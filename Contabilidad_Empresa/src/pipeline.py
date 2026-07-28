
#Objetivo: setar el orquestador
from conexion import engine
from extract import leer_csv
from transform import transformar_movimientos
from load import cargar_movimientos

ruta = "data/raw/movimientos.csv"
df = leer_csv(ruta)
df = transformar_movimientos(df)
cargar_movimientos(df, engine)
print("Proceso terminado")