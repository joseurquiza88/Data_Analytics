
#Objetivo: limpiar y preparar info antes de cargarla en PostgreSQL.
#Libreiras
import pandas as pd

def clasificar_movimiento(texto): # esto vino de la notebook de analisis de movimientos bancarios
    texto = str(texto).upper()
    if "TRANSFERENCIA REALIZADA" in texto or "DEBITO TRANSF." in texto:
        return "Transferencias realizadas"
    elif "TRANSFERENCIA RECIBIDA" in texto or "TRANSF RECIBIDA" in texto:
        return "Transferencias recibidas"
    elif "COMISION" in texto:
        return "Comisiones"
    elif "SIRCREB" in texto or "IMPUESTOS" in texto:
        return "Impuestos"
    elif "CHEQUE" in texto or " CH " in texto or "DEPOSITO ECHEQ" in texto or "DEPOSITO E-CHEQ" in texto:
        return "Cheques"
    elif "DEBITO AUTOMATICO" in texto:
        return "Debitos automaticos"
    elif "EXTRACCION" in texto:
        return "Extracciones"
    elif "DEPOSITO" in texto:
        return "Depositos"
    elif "INTERES" in texto:
        return "Intereses"
    elif "IVA 21%" in texto:
        return "Iva 21%"
    elif "PAGO DE SERVICIOS IMP. AFIP" in texto:
        return "Autonomos"
    else:
        return "Otros"
    
def transformar_movimientos(df):
    # Trabajar sobre una copia por las dudas
    df = df.copy()
    # Renombrar columnas
    df = df.rename(
        columns={
            "Fecha": "fecha",
            "Comprobante": "comprobante",
            "Movimiento": "movimiento",
            "Debito": "debito",
            "Credito": "credito",
            "Saldo en cuenta": "saldo_en_cuenta",
            "Mes": "mes",
            "Categoria": "categoria",
        }
    )

    # Convertir fecha
    df["fecha"] = pd.to_datetime(df["fecha"], format="%d/%m/%y", errors="coerce")

    # Crear mes a partir de fecha
    df["mes"] = df["fecha"].dt.strftime("%Y-%m")

    # Clasificar movimientos
    df["categoria"] = df["movimiento"].apply(clasificar_movimiento)
    # Limpiar comprobante
    df["comprobante"] = (df["comprobante"].replace("NA", "").fillna("").astype(str))

    # Convertir columnas numéricas
    df["debito"] = pd.to_numeric(df["debito"], errors="coerce")
    df["credito"] = pd.to_numeric(df["credito"],errors="coerce")
    df["saldo_en_cuenta"] = pd.to_numeric(df["saldo_en_cuenta"],errors="coerce")

    return df


# ------------------------------------------------------------------------------------------
# FACTURA EMITIDAS Y RECIBIDAS
def transformar_facturas (df, tipo):

    df = df.copy()

    columnas_monetarias = ["neto_gravado", "iva_10_5",  "iva_21",
        "iva_27", "iva_3", "percepcion_iibb", "percepcion_municipal", "no_gravado_exento","total"]

    for col in columnas_monetarias:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)


    columnas_opcionales = ["iva_10_5",  "iva_21","iva_27", "iva_3", "percepcion_iibb", "percepcion_municipal", "no_gravado_exento"]

    for col in columnas_opcionales:
        df[col] = df[col].fillna(0)

    # Fecha
    df["fecha"] = pd.to_datetime(df["fecha"],errors="coerce", dayfirst=True)

    # Mes
    df["mes"] = df["fecha"].dt.strftime("%Y-%m")

    # CUIT
    df["cuit"] = (df["cuit"].astype("string").str.replace("-", "", regex=False).str.replace(".0", "", regex=False).str.strip())

    # Columnas texto comunes
    columnas_texto = [ "razon_social", "tipo_comprobante"]

    # Columnas particulares
    if tipo == "compras":
        columnas_texto += [ "concepto", "forma_pago", "condicion"]

    elif tipo == "ventas":
        columnas_texto += ["forma_cobro"]
    else:
        raise ValueError("Tipo debe ser compras o ventas")

    for col in columnas_texto:
        df[col] = (df[col].astype("string").fillna("").str.strip().str.upper())


    return df

  