from pathlib import Path

import pandas as pd
import streamlit as st

# Título de la app
st.title("Mi primera app con Streamlit")

# Ruta del archivo datos.csv (en la misma carpeta que app.py)
ruta = Path(__file__).parent / "datos.csv"

# Cargar el archivo con pandas
try:
    df = pd.read_csv(ruta)
except FileNotFoundError:
    st.error("No encontré el archivo datos.csv. Verifica que esté en la misma carpeta que app.py.")
    st.stop()

# Verificar que existan las columnas necesarias
columnas_necesarias = ["total", "categoria", "fecha"]
faltantes = [c for c in columnas_necesarias if c not in df.columns]
if faltantes:
    st.error(f"Faltan estas columnas en datos.csv: {', '.join(faltantes)}")
    st.write("Columnas que encontré:", list(df.columns))
    st.stop()

# Convertir tipos de datos
df["total"] = pd.to_numeric(df["total"], errors="coerce")
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

# Quitar filas sin fecha válida (no se pueden filtrar por fecha)
df = df.dropna(subset=["fecha"])
if df.empty:
    st.error("No hay fechas válidas en la columna 'fecha'.")
    st.stop()

# ---------------- BARRA LATERAL: FILTROS ----------------
st.sidebar.header("Filtros")

# 1) Filtro de rango de fechas
fecha_min = df["fecha"].min().date()
fecha_max = df["fecha"].max().date()

rango = st.sidebar.date_input(
    "Rango de fechas",
    value=(fecha_min, fecha_max),
    min_value=fecha_min,
    max_value=fecha_max,
)

# date_input devuelve una sola fecha mientras el usuario no eligió la segunda
if isinstance(rango, (tuple, list)) and len(rango) == 2:
    fecha_inicio, fecha_fin = rango
else:
    st.sidebar.info("Elige la fecha de inicio y la de fin.")
    st.stop()

# 2) Filtro de categorías (una o varias)
categorias_disponibles = sorted(df["categoria"].dropna().unique())
categorias_elegidas = st.sidebar.multiselect(
    "Categorías",
    options=categorias_disponibles,
    default=categorias_disponibles,
)

# ---------------- APLICAR FILTROS ----------------
df_filtrado = df[
    (df["fecha"].dt.date >= fecha_inicio)
    & (df["fecha"].dt.date <= fecha_fin)
    & (df["categoria"].isin(categorias_elegidas))
]

if df_filtrado.empty:
    st.warning("No hay datos con los filtros elegidos. Prueba con otro rango o más categorías.")
    st.stop()

# Mostrar cantidad de filas y columnas (de los datos filtrados)
filas, columnas = df_filtrado.shape
st.write(f"Con los filtros actuales hay **{filas}** filas y **{columnas}** columnas.")

# 1) Métrica grande con el total de ventas
total_ventas = df_filtrado["total"].sum()
st.metric(label="Total de ventas", value=f"{total_ventas:,.2f}")

# 2) Gráfico de barras: total vendido por categoría
st.subheader("Total vendido por categoría")
ventas_categoria = (
    df_filtrado.groupby("categoria")["total"].sum().sort_values(ascending=False)
)
st.bar_chart(ventas_categoria)

# 3) Gráfico de líneas: evolución del total por fecha
st.subheader("Evolución del total por fecha")
ventas_fecha = df_filtrado.groupby("fecha")["total"].sum().sort_index()
st.line_chart(ventas_fecha)

# Mostrar la tabla (filtrada)
st.subheader("Tabla filtrada")
st.dataframe(df_filtrado)