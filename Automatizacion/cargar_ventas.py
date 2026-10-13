# Prueba de cargar los datos manualmente en un csv
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, URL

# 1. Cargar las variables de conexión
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

# 2. Definir la ubicación de los CSV
CARPETA_DATOS = Path(__file__).parent / "data"
ARCHIVO_ORDERS = CARPETA_DATOS / "orders.csv"
ARCHIVO_ITEMS = CARPETA_DATOS / "order_items.csv"


def cargar_ventas():
    # 3. Leer los archivos
    orders = pd.read_csv(ARCHIVO_ORDERS)
    items = pd.read_csv(ARCHIVO_ITEMS)

    # 4. Validar las columnas necesarias
    columnas_orders = {"order_id", "customer_id", "order_status", "order_purchase_timestamp", "order_approved_at", 
        "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date",}

    columnas_items = { "order_id", "order_item_id", "product_id", "seller_id", "shipping_limit_date", "price","freight_value",}

    if not columnas_orders.issubset(orders.columns):
        raise ValueError("Faltan columnas requeridas en orders.csv")

    if not columnas_items.issubset(items.columns):
        raise ValueError("Faltan columnas requeridas en order_items.csv")

    # 5. Convertir fechas
    columnas_fecha_orders = ["order_purchase_timestamp", "order_approved_at",  "order_delivered_carrier_date", "order_delivered_customer_date",]
    for columna in columnas_fecha_orders:
        orders[columna] = pd.to_datetime(orders[columna], dayfirst=True, errors="raise", )

        orders["order_estimated_delivery_date"] = pd.to_datetime( orders["order_estimated_delivery_date"],dayfirst=True, errors="raise",).dt.date

        items["shipping_limit_date"] = pd.to_datetime(items["shipping_limit_date"], dayfirst=True, errors="raise",)

    # 6. Validar identificadores duplicados dentro de los CSV
    if orders["order_id"].duplicated().any():
        raise ValueError("Hay order_id duplicados en orders.csv")

    if items.duplicated(["order_id", "order_item_id"]).any():
        raise ValueError(
            "Hay combinaciones duplicadas de order_id y order_item_id"
        )

    # 7. Cargar los datos dentro de una transacción
    # Si algo falla, se revierten ambas cargas.
    with engine.begin() as conexion:
        # Insertar primero los pedidos
        conexion.execute(
            text("""
                INSERT INTO public.orders_prueba (
                    order_id,
                    customer_id,
                    order_status,
                    order_purchase_timestamp,
                    order_approved_at,
                    order_delivered_carrier_date,
                    order_delivered_customer_date,
                    order_estimated_delivery_date
                )
                VALUES (
                    :order_id,
                    :customer_id,
                    :order_status,
                    :order_purchase_timestamp,
                    :order_approved_at,
                    :order_delivered_carrier_date,
                    :order_delivered_customer_date,
                    :order_estimated_delivery_date
                )
                ON CONFLICT (order_id) DO NOTHING
            """),
            orders.to_dict(orient="records"),
        )

        # Insertar después los artículos
        conexion.execute(
            text("""
                INSERT INTO public.order_items_prueba (
                    order_id,
                    order_item_id,
                    product_id,
                    seller_id,
                    shipping_limit_date,
                    price,
                    freight_value
                )
                VALUES (
                    :order_id,
                    :order_item_id,
                    :product_id,
                    :seller_id,
                    :shipping_limit_date,
                    :price,
                    :freight_value
                )
                ON CONFLICT (order_id, order_item_id) DO NOTHING
            """),
            items.to_dict(orient="records"),
        )

    print(f"Pedidos leídos desde CSV: {len(orders)}")
    print(f"Artículos leídos desde CSV: {len(items)}")
    print("Carga finalizada correctamente.")


if __name__ == "__main__":
    try:
        cargar_ventas()
    except Exception as error:
        print(f"Error durante la carga: {error}")
    finally:
        engine.dispose()