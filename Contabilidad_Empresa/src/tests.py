# Objetivo validar la info que se sube
def validar_dataframe(df):
    assert not df.empty
    columnas = [ "fecha", "movimiento", "debito", "credito","archivo_origen", "categoria" ]
    for col in columnas:
        assert col in df.columns
    assert df["fecha"].notna().all()
    return True