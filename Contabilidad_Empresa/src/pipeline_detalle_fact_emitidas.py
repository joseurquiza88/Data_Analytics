from pathlib import Path
from src.conexion import engine
from src.extract import extraer_detalle_fact_emitidas
from src.transform import transformar_detalle_fact_emitidas
from src.load import cargar_detalle_fact_emitidas
from src.tests import test_detalle_fact_emitidas


CARPETA_EXCEL = Path("data/raw/facturas")


def pipeline_detalle_fact_emitidas():
    archivos = sorted(CARPETA_EXCEL.glob("*.pdf"))
    for archivo in archivos:
        print(f"\nProcesando archivo: {archivo.name}")
        # Extract
        df= extraer_detalle_fact_emitidas(archivo)
        df_detalle_fact_emitidas = extraer_detalle_fact_emitidas(archivo)

        print(df_detalle_fact_emitidas)
        print(df_detalle_fact_emitidas.columns)
        print("Cantidad registros:", len(df_detalle_fact_emitidas))
        # Transform
        df_detalle_fact_emitidas= transformar_detalle_fact_emitidas(df_detalle_fact_emitidas)
        # Tests
        test_detalle_fact_emitidas(df_detalle_fact_emitidas)
        # Load
        cargar_detalle_fact_emitidas(df_detalle_fact_emitidas, engine)
