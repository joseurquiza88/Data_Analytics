# Programa de monitoreo de ventas semanal

#Librerias
import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
import smtplib
from email.message import EmailMessage
from textwrap import dedent
# 1. Configuración de la conexión
load_dotenv()

url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST", "localhost"),
    port=int(os.getenv("DB_PORT", "5432")),
    database=os.getenv("DB_NAME", "olist"),)

engine = create_engine(url)


# 2. Extracción de datos
# SELECT DATE_TRUNC('month', o.order_purchase_timestamp)::date AS mes, COUNT(DISTINCT o.order_id) AS pedidos_entregados,
def obtener_ventas_semanal(engine):
    query = """
        SELECT DATE_TRUNC('week', o.order_purchase_timestamp)::date AS semana, COUNT(DISTINCT o.order_id) AS pedidos_entregados,
        
            SUM(oi.price) AS facturacion_productos, SUM(oi.price) / NULLIF(COUNT(DISTINCT o.order_id), 0) AS ticket_promedio
        FROM orders_prueba AS o
        INNER JOIN order_items_prueba AS oi
            ON o.order_id = oi.order_id
        WHERE o.order_status = 'delivered'
        GROUP BY DATE_TRUNC('week', o.order_purchase_timestamp)::date
        ORDER BY semana;
    """

    return pd.read_sql(query, engine)


# 3. Calculo de indicadores y detección de alertas
umbral = -20
def ejecutar_monitoreo(engine, umbral_caida=umbral):

    ventas = obtener_ventas_semanal(engine)

    ventas["semana"] = pd.to_datetime(ventas["semana"])
    ventas = ventas.sort_values("semana").copy()

    facturacion_por_semana = ventas.set_index("semana")["facturacion_productos"]

    semana_anterior = ventas["semana"] - pd.DateOffset(weeks=1)

    ventas["facturacion_semana_anterior"] = semana_anterior.map(facturacion_por_semana)

    ventas["variacion_pct"] = round((ventas["facturacion_productos"] / ventas["facturacion_semana_anterior"] - 1) * 100,2)

    alertas = ventas[ventas["variacion_pct"].notna() & (ventas["variacion_pct"] < umbral_caida)].copy()

    return ventas, alertas

# 4. Enviar mail
def enviar_email(asunto, cuerpo):
    remitente = os.getenv("EMAIL_REMITENTE")
    destinatario = os.getenv("EMAIL_DESTINATARIO")
    password = os.getenv("EMAIL_PASSWORD")
    servidor = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    puerto = int(os.getenv("SMTP_PORT", "587"))

    if not remitente or not destinatario or not password:
        raise ValueError(
            "Faltan variables de correo en el archivo .env."
        )

    mensaje = EmailMessage()
    mensaje["Subject"] = asunto
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje.set_content(cuerpo)

    with smtplib.SMTP(servidor, puerto) as smtp:
        smtp.starttls()
        smtp.login(remitente, password)
        smtp.send_message(mensaje)

    print("Correo de alerta enviado correctamente.")






# 5. Ejecución del proceso
def main():
    try:
        ventas, alertas = ejecutar_monitoreo(engine)
        print(ventas[["semana","pedidos_entregados","facturacion_productos","facturacion_semana_anterior","variacion_pct",]].to_string(index=False))

        print(f"Semanas analizadas: {len(ventas)}")
        print(f"Alertas detectadas: {len(alertas)}")

        if alertas.empty:
            print("No se detectaron caídas superiores al umbral.")

        else:
            for _, fila in alertas.iterrows():

                semana = fila["semana"].strftime("%d/%m/%Y")
                facturacion_actual = fila["facturacion_productos"]
                facturacion_anterior = fila["facturacion_semana_anterior"]
                variacion = fila["variacion_pct"]

                print(
                    f"ALERTA | Semana del {semana}: "
                    f"caída del {abs(variacion):.2f}% "
                    "respecto de la semana anterior."
                )

                asunto = f"ALERTA: caída de ventas del {abs(variacion):.2f}%"

                cuerpo = dedent(f"""
                    Se detectó una caída en la facturación semanal.

                    Semana analizada: {semana}
                    Facturación de la semana anterior: ${facturacion_anterior:,.2f}
                    Facturación de la semana actual: ${facturacion_actual:,.2f}
                    Variación semanal: {variacion:.2f}%

                    Umbral configurado: {umbral}%

                    Este correo fue generado automáticamente por el sistema
                    de monitoreo de ventas.
                """).strip()

                enviar_email(asunto, cuerpo)

    finally:
        engine.dispose()


if __name__ == "__main__":
    main()


    # Para correrlo
    # python monitoreo_ventas.py