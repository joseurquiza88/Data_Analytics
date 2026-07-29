
# Objetivo: setar el orquestador
# Pipeline completo de carga de resumenes bancarios 
# Objetivo de la funcion:
# - Buscar todos los PDF de la carpeta raw
# - Extraer los movimientos
# - Validar el resumen
# - Transformar los datos
# - Cargar a PostgreSQL
# - Mostrar un resumen del proceso


from pathlib import Path
from conexion import engine
from extract import extraer_movimientos_pdf
from transform import transformar_movimientos
from load import cargar_movimientos
from tests import validar_dataframe

# Carpeta donde se encuentran los resúmenes bancarios
CARPETA_PDF = Path("data/raw/resumenes_bancarios")

def pipeline_movBancarios():
    # Buscar todos los PDF
    pdfs = sorted(CARPETA_PDF.glob("*.pdf"))
    if not pdfs:
        print("No se encontraron archivos PDF para procesar.")
        return

    archivos_ok = 0
    archivos_omitidos = 0
    archivos_error = 0

    print("=" * 60)
    print("INICIO DEL PROCESO")
    print("=" * 60)

    # Recorrer todos los PDF encontrados
    for pdf in pdfs:

        print(f"\nProcesando archivo: {pdf.name}")
        # Extraccion
        df, validacion = extraer_movimientos_pdf(pdf)
        print(f"Movimientos encontrados: {len(df)}")

        # Validacion
        if not validacion:
            print("El archivo no pasó la validación.")
            archivos_error += 1
            continue

        # Transformacion
        df = transformar_movimientos(df)
        print(df.columns.tolist())
        validar_dataframe(df)
        # Load
        cargado = cargar_movimientos(df, engine)

        if cargado:
            archivos_ok += 1
        else:
            archivos_omitidos += 1

    # Resumen final del procesamiento
    print("\n" + "=" * 60)
    print("Resumen del proceso")
    print("=" * 60)
    print(f"Archivos encontrados : {len(pdfs)}")
    print(f"Archivos cargados    : {archivos_ok}")
    print(f"Archivos omitidos    : {archivos_omitidos}")
    print(f"Archivos con error   : {archivos_error}")
    print("=" * 60)


# ------------------------------------------------------------------------------------------
# FACTURA EMITIDAS Y RECIBIDAS