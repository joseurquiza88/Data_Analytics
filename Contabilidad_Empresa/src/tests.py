# Test ETL
# Objetivo: Validar la calidad de los datos antes de cargarlos en PostgreSQL.
# =====================================================

import pandas as pd
from pandas.api.types import is_datetime64_any_dtype

def validar_dataframe(df):

    print("=" * 50)
    print("VALIDANDO DATAFRAME")
    print("=" * 50)

    # 1. DataFrame no vacío
    assert not df.empty, "El DataFrame está vacío."
    print(" DataFrame no vacío.")

    # 2. Columnas esperadas
    columnas_esperadas = ["fecha", "comprobante", "movimiento", "debito", "credito", "saldo_en_cuenta",
    "archivo_origen", "mes", "categoria"]
    faltantes = set(columnas_esperadas) - set(df.columns)
    assert len(faltantes) == 0, (f"Faltan columnas: {faltantes}")

    print("Columnas correctas.")

    # 3. Sin filas duplicadas
    duplicados = df.duplicated().sum()
    assert duplicados == 0, (f"Existen {duplicados} filas duplicadas.")


    print("Sin registros duplicados.")

    # 4. Fechas válidas
    assert is_datetime64_any_dtype(df["fecha"]), \
    "La columna fecha no es de tipo datetime."

    print("Fechas válidas.")
    
    # 5. Columnas numéricas
    for columna in ["debito", "credito", "saldo_en_cuenta"]:
        assert pd.api.types.is_numeric_dtype(df[columna]), (f"{columna} no es numerica."        )

    print("Tipos de datos numericos correctos.")

    # 6. Sin nulos en columnas críticas
    columnas_criticas = ["fecha", "movimiento", "saldo_en_cuenta", "archivo_origen"]

    for columna in columnas_criticas:
        nulos = df[columna].isna().sum()
        assert nulos == 0, (f" {columna} tiene {nulos} valores nulos." )

    print("Sin valores nulos críticos.")

    # 7. Debito y Credito no pueden coexistir
    inconsistentes = ((df["debito"] > 0) & (df["credito"] > 0)).sum()
    assert inconsistentes == 0, (f"Hay {inconsistentes} movimientos con debito y credito simultaneamente.")
    print("Movimientos consistentes.")

    # 8. Importes negativos
    assert (df["debito"].dropna() >= 0).all(), ("Existen debitos negativos.")
    assert (df["credito"].dropna() >= 0).all(), (" Existen creditos negativos.")
    print("Sin importes negativos.")

    # 9. Saldo informado
    assert (df["saldo_en_cuenta"] != 0).all(), ("Existen saldos iguales a cero.")

    print("Saldos validos.")

    # 10. Archivo origen
    assert (df["archivo_origen"].astype(str).str.len().gt(0).all()), "Hay registros sin archivo de origen."

    print("Trazabilidad correcta.")

    # Resumen
    print("=" * 50)
    print("TODAS LAS VALIDACIONES FUERON EXITOSAS")
    print("=" * 50)


# ------------------------------------------------------------------------------------------
# FACTURA EMITIDAS Y RECIBIDAS
def test_facturas(df, tipo):
    print("=" * 50)
    print("VALIDANDO DATAFRAME")
    print("=" * 50)

    # 1. DataFrame no vacío
    assert not df.empty, "El DataFrame está vacío."
    print(" DataFrame no vacío.")


    if tipo == "ventas":

        columnas_esperadas = ['fecha', 'tipo_comprobante', 'punto_venta', 'numero_comprobante',
       'razon_social', 'cuit', 'neto_gravado', 'iva_10_5', 'iva_21', 'iva_27',
       'iva_3', 'percepcion_iibb', 'percepcion_municipal', 'no_gravado_exento',
       'total', 'forma_cobro', 'archivo_origen']

    elif tipo == "compras":

        columnas_esperadas = ['fecha', 'tipo_comprobante', 'punto_venta', 'numero_comprobante',
           'razon_social', 'cuit', 'neto_gravado', 'iva_10_5', 'iva_21', 'iva_27',
           'iva_3', 'percepcion_iibb', 'percepcion_municipal', 'no_gravado_exento',
           'total', 'forma_pago', 'archivo_origen']

    else:
        raise ValueError("Tipo debe ser compras o ventas")
    faltantes = set(columnas_esperadas) - set(df.columns)
    assert len(faltantes) == 0, f"Faltan columnas: {faltantes}"
    print("Columnas correctas de compras y/o ventas.")

    # Test sobre los formatos numericos, string y date
    assert is_datetime64_any_dtype(df["fecha"]), \
    "La columna fecha no es de tipo datetime."
    print("Fechas válidas.")


    # Columnas numéricas
    for columna in ['neto_gravado', 'iva_10_5', 'iva_21', 'iva_27',
           'iva_3', 'percepcion_iibb', 'percepcion_municipal', 'no_gravado_exento',
           'total']:
        assert pd.api.types.is_numeric_dtype(df[columna]), (f"{columna} no es numerica."        )

    print("Tipos de datos numericos correctos.")

    # Columnas string
    columnas_string = ['tipo_comprobante', 'razon_social',
                       'cuit', 'archivo_origen']

    if tipo == "compras":
        columnas_string += ['condicion','concepto','forma_pago']

    elif tipo == "ventas":
        columnas_string += ['forma_cobro']
    for columna in columnas_string:
        assert pd.api.types.is_string_dtype(df[columna])

    print("Tipos de datos string correctos.")

    #Test del tipo de fecha
    fecha_futura = df["fecha"] > pd.Timestamp.today()
    assert not fecha_futura.any(), "Hay fechas futuras"
    print("Fechas dentro del rango esperado.")

    #Test de que esten todas las fechas, no haya vacios y que esten en formato fecha
    columnas_criticas = ['fecha', 'tipo_comprobante', 'punto_venta', 'numero_comprobante',
       'razon_social', 'neto_gravado', 'total', 'archivo_origen']
    if tipo == "compras":
        columnas_criticas += ["cuit",'condicion','concepto', 'forma_pago']
    if tipo == "ventas":
        columnas_criticas += ['forma_cobro']
    for columna in columnas_criticas:
        nulos = df[columna].isna().sum()
        assert nulos == 0, (f"{columna} tiene {nulos} valores nulos")

    print("Sin valores nulos críticos.")

    # Test de archivo origen
    assert (df["archivo_origen"].astype(str).str.len().gt(0).all()), "Hay registros sin archivo de origen."

    print("Trazabilidad correcta.")

    # Test de que la suma de todos los valores monetario sean = al total
    total_calculado = (df["neto_gravado"] + df["iva_21"] + df["iva_10_5"] + df["iva_27"] +
                        df["iva_3"]+ df["percepcion_iibb"] + df["percepcion_municipal"] +
                         df["no_gravado_exento"])
    diferencia = abs(total_calculado - df["total"])
    assert (diferencia < 1).all(), "Hay facturas donde no coincide el total."

    # Test de info duplicada
    duplicados = df.duplicated(subset=["fecha","tipo_comprobante",  "punto_venta", "numero_comprobante" ]).sum()
    assert duplicados == 0, f"Hay {duplicados} comprobantes duplicados"



   # Test de CUIT
    if tipo == "compras": 
        cuit_vacio = df["cuit"].isna().sum()
        assert cuit_vacio == 0, "Hay compras sin CUIT"
        cuit_incorrecto = df["cuit"].astype(str).str.len() != 11
        assert not cuit_incorrecto.any(), "Hay CUIT de compras con longitud incorrecta"

    elif tipo == "ventas":
        cuit_con_dato = (df["cuit"].dropna().astype(str).str.strip())
        cuit_con_dato = cuit_con_dato[cuit_con_dato != ""]
        cuit_incorrecto = cuit_con_dato.astype(str).str.len() != 11
        if cuit_incorrecto.any(): 
            print("CUIT problemáticos:")
            print(cuit_con_dato[cuit_incorrecto].unique())

        assert not cuit_incorrecto.any(), \
            "Hay CUIT informados con longitud incorrecta"


    # Resumen
    print("=" * 50)
    print("TODAS LAS VALIDACIONES FUERON EXITOSAS")
    print("=" * 50)


# ------------------------------------------------------------------------------------------
# Detalle de productos obtenidos de las facturas emititas

def test_detalle_fact_emitidas(df):

    #DataFrame no vacío
    assert not df.empty, "El DataFrame está vacío."
    print(" DataFrame no vacío.")

    #columnas esperadas
    columnas_esperadas =  ["cliente_doc", "fecha_venta", "mes", "punto_venta", "comp_nro", "razon_social", 
"condicion_iva", "domicilio", "condicion_venta", "producto", "cantidad", "unidad", 
"precio_unitario", "bonificacion", "importe_bonificacion", "subtotal", "archivo_origen"]

    faltantes = set(columnas_esperadas) - set(df.columns)
    assert len(faltantes) == 0, f"Faltan columnas: {faltantes}"
    print("Columnas correctas del detalle de las facturas emitidas")


    # Columnas numéricas
    columnas_numericas = ['cantidad', 'precio_unitario', "bonificacion", "importe_bonificacion", "subtotal"]:
    for columna in columnas_numericas:
        assert pd.api.types.is_numeric_dtype(df[columna]), f"{columna} no es numérica."
        print("Tipos de datos numéricos correctos.")
        assert pd.api.types.is_string_dtype(df[columna])
        print("Tipos de datos string correctos.")


    # Columnas string
    columnas_string = ["cliente_doc", "punto_venta", "comp_nro", "razon_social",
        "condicion_iva", "domicilio", "condicion_venta", "producto", "unidad", "archivo_origen", "mes"]
    for columna in columnas_string:
        assert pd.api.types.is_string_dtype(df[columna]), f"{columna} no es de tipo string."
    print("Tipos de datos string correctos.")

    # Productos no vacíos
    assert (df["producto"].str.strip() != "").all()

    # Cantidad positiva
    assert (df["cantidad"] > 0).all()

    # Precio unitario no negativo
    assert (df["precio_unitario"] >= 0).all()


    # Subtotal no negativo
    assert (df["subtotal"] >= 0).all()

    # Subtotal no negativo
    assert (df["bonificacion"] >= 0).all()

    #Test del tipo de fecha
    fecha_futura = df["fecha"] > pd.Timestamp.today()
    assert not fecha_futura.any(), "Hay fechas futuras"
    print("Fechas dentro del rango esperado.")

    #Informacion duplicado
    duplicados = df.duplicated(subset=["fecha_venta","punto_venta",  "comp_nro", "producto" ]).sum()
    assert duplicados == 0, f"Hay {duplicados} comprobantes duplicados"

    # Mes consistente con la fecha
    mes_calculado = df["fecha_venta"].dt.strftime("%Y-%m")
    assert (mes_calculado == df["mes"]).all()