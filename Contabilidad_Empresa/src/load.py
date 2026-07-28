## Objetivo: cargar informacion a postgress SQL

from sqlalchemy import text
import pandas as pd
# Se coloca en la base de datosde postrgress
def cargar_movimientos(df, engine):
    print("Columnas a cargar:")
    print(df.columns.tolist())
    df.to_sql("movimientos_bancarios", engine, if_exists="append", index=False)

#Funcion para hacer consultas
def consultar_sql(sql, engine):
    return pd.read_sql(text(sql), engine)