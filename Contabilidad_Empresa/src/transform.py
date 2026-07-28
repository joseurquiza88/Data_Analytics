
#Objetivo: limpiar y preparar info
import pandas as pd
def transformar_movimientos(df):
    df = df.rename(
        columns={
            "Fecha":"fecha",
            "Comprobante":"comprobante",
            "Movimiento":"movimiento",
            "Debito":"debito",
            "Credito":"credito",
            "Saldo en cuenta":"saldo_en_cuenta"
        }
    )

    df["fecha"] = pd.to_datetime(df["fecha"], format="%d/%m/%Y")

    return df