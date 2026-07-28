## Objetivo: sacar datos de una fuente

def leer_csv(ruta):
    import pandas as pd
    df = pd.read_csv(ruta)
    return df