from pathlib import Path
from src.conexion import engine
from src.extract import extraer_facturas_excel
from src.transform import transformar_facturas
from src.load import (cargar_facturas_recibidas, cargar_facturas_emitidas)
from src.tests import test_facturas


CARPETA_EXCEL = Path("data/raw/contabilidad")


def pipeline_facturas():
    archivos = sorted(CARPETA_EXCEL.glob("*.xlsx"))

    for archivo in archivos:

        print(f"\nProcesando archivo: {archivo.name}")

        # Extract
        df_compras, df_ventas = extraer_facturas_excel(archivo)

        # Transform
        df_compras = transformar_facturas(df_compras, "compras")
        df_ventas = transformar_facturas(df_ventas, "ventas")

        # Tests
        test_facturas(df_compras, "compras")
        test_facturas(df_ventas, "ventas")

        # Load
        cargar_facturas_recibidas(df_compras, engine)
        cargar_facturas_emitidas(df_ventas, engine)