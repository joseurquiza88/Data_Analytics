## Objetivo: cargar informacion a postgress SQL

from sqlalchemy import text
import pandas as pd
# Se coloca en la base de datosde postrgress
# def cargar_movimientos(df, engine):
#     print("Columnas a cargar:")
#     print(df.columns.tolist())
#     df.to_sql("movimientos_bancarios", engine, if_exists="append", index=False)

def cargar_movimientos(df, engine):

    archivo = df["archivo_origen"].iloc[0]

    consulta = """
    SELECT COUNT(*)
    FROM movimientos_bancarios
    WHERE archivo_origen = :archivo
    """

    with engine.connect() as conexion:

        resultado = conexion.execute(text(consulta),{"archivo": archivo})
        existe = resultado.scalar()

    if existe > 0:
        print(f"Archivo ya cargado: {archivo}")
        return False

    df.to_sql("movimientos_bancarios", engine, if_exists="append", index=False)
    print(f"Archivo cargado correctamente: {archivo}")
    return True

#Funcion para hacer consultas
def consultar_sql(sql, engine):
    return pd.read_sql(text(sql), engine)



# ------------------------------------------------------------------------------------------
# FACTURA EMITIDAS Y RECIBIDAS

def cargar_facturas_recibidas(df, engine):

    archivo = df["archivo_origen"].iloc[0]

    consulta = """
    SELECT COUNT(*)
    FROM fact_recibidas
    WHERE archivo_origen = :archivo
    """

    with engine.connect() as conexion:

        resultado = conexion.execute(text(consulta),{"archivo": archivo})
        existe = resultado.scalar()

    if existe > 0:
        print(f"Compras ya cargadas: {archivo}")
        return False

    df.to_sql("fact_recibidas", engine, if_exists="append", index=False)
    print(f"Compras cargadas correctamente: {archivo}. Registros insertados: {len(df)}")
    return True


def cargar_facturas_emitidas(df, engine):

    archivo = df["archivo_origen"].iloc[0]

    consulta = """
    SELECT COUNT(*)
    FROM fact_emitidas
    WHERE archivo_origen = :archivo
    """

    with engine.connect() as conexion:

        resultado = conexion.execute(text(consulta),{"archivo": archivo})
        existe = resultado.scalar()

    if existe > 0:
        print(f"Ventas ya cargadas: {archivo}")
        return False

    df.to_sql("fact_emitidas", engine, if_exists="append", index=False)
    print(f"Ventas cargadas correctamente: {archivo}. Registros insertados: {len(df)}")
    return True

