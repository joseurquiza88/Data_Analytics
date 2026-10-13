import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL


# 1. Configuración de la conexión
load_dotenv()

url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME", "olist"),
)

engine = create_engine(url)


# 2. Extracción de datos
def obtener_ventas_mensuales(engine):
    query = """
        SELECT
            DATE_TRUNC(
                'month', o.order_purchase_timestamp
            )::date AS mes,
            COUNT(DISTINCT o.order_id) AS pedidos_entregados,
            SUM(oi.price) AS facturacion_productos,
            SUM(oi.price) /
                NULLIF(COUNT(DISTINCT o.order_id), 0)
                AS ticket_promedio
        FROM orders AS o
        INNER JOIN order_items AS oi
            ON o.order_id = oi.order_id
        WHERE o.order_status = 'delivered'
        GROUP BY
            DATE_TRUNC(
                'month', o.order_purchase_timestamp
            )::date
        ORDER BY mes;
    """

    return pd.read_sql(query, engine)


# 3. Cálculo de indicadores y detección de alertas
def ejecutar_monitoreo(engine, umbral_caida=-15):
    ventas = obtener_ventas_mensuales(engine)

    ventas["mes"] = pd.to_datetime(ventas["mes"])
    ventas = ventas.sort_values("mes").copy()

    facturacion_por_mes = ventas.set_index("mes")[
        "facturacion_productos"
    ]

    mes_anterior = ventas["mes"] - pd.DateOffset(months=1)

    ventas["facturacion_mes_anterior"] = mes_anterior.map(
        facturacion_por_mes
    )

    ventas["variacion_pct"] = (
        ventas["facturacion_productos"]
        / ventas["facturacion_mes_anterior"]
        - 1
    ) * 100

    alertas = ventas[
        ventas["variacion_pct"].notna()
        & (ventas["variacion_pct"] < umbral_caida)
    ].copy()

    return ventas, alertas


# 4. Ejecución del proceso
def main():
    try:
        ventas, alertas = ejecutar_monitoreo(engine)

        print(f"Meses analizados: {len(ventas)}")
        print(f"Alertas detectadas: {len(alertas)}")

        if alertas.empty:
            print("No se detectaron caídas superiores al umbral.")
        else:
            for _, fila in alertas.iterrows():
                print(
                    f"ALERTA | {fila['mes']:%m/%Y}: "
                    f"caída del {abs(fila['variacion_pct']):.2f}% "
                    "respecto del mes anterior."
                )

    finally:
        engine.dispose()


if __name__ == "__main__":
    main()