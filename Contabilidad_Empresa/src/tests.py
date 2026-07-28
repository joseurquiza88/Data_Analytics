# TESTS
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