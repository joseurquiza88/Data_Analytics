## Objetivo: cargar informacion a postgress SQL

def cargar_movimientos(df, engine):
    df.to_sql("movimientos_bancarios", engine, if_exists="append", index=False)