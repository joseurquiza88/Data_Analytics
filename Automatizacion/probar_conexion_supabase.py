import os
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine, text

load_dotenv()

url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("SUPABASE_DB_USER"),
    password=os.getenv("SUPABASE_DB_PASSWORD"),
    host=os.getenv("SUPABASE_HOST"),
    port=int(os.getenv("SUPABASE_PORT", "6543")),
    database=os.getenv("SUPABASE_DB_NAME", "postgres"),
    query={"sslmode": "require"},
)

engine = create_engine(url)

try:
    with engine.connect() as connection:
        resultado = connection.execute(
            text("""
                SELECT
                    (SELECT COUNT(*) FROM public.orders_prueba) AS pedidos,
                    (SELECT COUNT(*) FROM public.order_items_prueba) AS detalles
            """)
        ).one()

        print("Conexión a Supabase exitosa.")
        print(f"Pedidos: {resultado.pedidos}")
        print(f"Detalles: {resultado.detalles}")

finally:
    engine.dispose()