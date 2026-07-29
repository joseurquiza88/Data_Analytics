
import streamlit as st
import pandas as pd
from datetime import datetime

from src.pipeline_movBancarios import pipeline_movBancarios
from src.pipeline_facturas import pipeline_facturas
from src.conexion import engine


# Configuración
st.set_page_config(page_title="Contabilidad",page_icon="📊",layout="wide")

# Titulo
st.title("Sistema de Contabilidad")
st.caption("Pipeline ETL - Extracción, Transformación, Validación y Carga")
st.divider()


# SIDEBAR


st.sidebar.title("Procesamiento")

opcion = st.sidebar.radio(
    "Seleccionar proceso",
    ["Resumen","Movimientos Bancarios","Facturas", "Ejecutar Todo"])


# RESUMEN
if opcion == "Resumen":
    st.subheader("Resumen del sistema")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric( "Estado ETL", "Listo")

    with col2:
        st.metric( "Base de datos","PostgreSQL")

    with col3:st.metric("Última ejecución",datetime.now().strftime("%d/%m/%Y"))

    st.divider()
    st.subheader("📂 Información disponible")
    try:
        # Consulta movimientos bancarios
        banco = pd.read_sql(
            """
            SELECT 
                MIN(fecha) AS desde,
                MAX(fecha) AS hasta,
                COUNT(*) AS registros
            FROM movimientos_bancarios
            """,
            engine
        )

        # Consulta facturas recibidas
        compras = pd.read_sql(
            """
            SELECT 
                MIN(fecha) AS desde,
                MAX(fecha) AS hasta,
                COUNT(*) AS registros
            FROM fact_recibidas
            """,
            engine
        )

        # Consulta facturas emitidas
        ventas = pd.read_sql(
            """
            SELECT 
                MIN(fecha) AS desde,
                MAX(fecha) AS hasta,
                COUNT(*) AS registros
            FROM fact_emitidas
            """,
            engine
        )
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### Movimientos Bancarios")
            st.metric("Registros",int(banco["registros"].iloc[0]))
            if banco["desde"].iloc[0]:
                st.write(
                    f"""
                     Desde: {banco["desde"].iloc[0].strftime('%d/%m/%Y')}
                    Hasta: {banco["hasta"].iloc[0].strftime('%d/%m/%Y')}
                    """)
        with col2:
            st.markdown("### 🧾 Facturas Recibidas")
            st.metric("Registros",int(compras["registros"].iloc[0]))
            if compras["desde"].iloc[0]:
                st.write(
                    f"""
                    Desde: {compras["desde"].iloc[0].strftime('%d/%m/%Y')}
                    Hasta: {compras["hasta"].iloc[0].strftime('%d/%m/%Y')}
                    """)
        with col3:
            st.markdown("### 💰 Facturas Emitidas")
            st.metric( "Registros", int(ventas["registros"].iloc[0]))
            if ventas["desde"].iloc[0]:
                st.write(
                    f"""
                    Desde: {ventas["desde"].iloc[0].strftime('%d/%m/%Y')}
                    Hasta: {ventas["hasta"].iloc[0].strftime('%d/%m/%Y')}
                    """
                )
        st.divider()
        st.info(
            """
            El sistema contiene información procesada desde:
            - Extractos bancarios PDF
            - Facturas de compra (recibidas)
            - Facturas de venta (emitidas)
            Los datos fueron extraídos, transformados,
            validados y cargados en PostgreSQL.
            """
        )

    except Exception as e:
        st.warning(f"No fue posible consultar la información disponible: {e}")

#Banco


elif opcion == "Movimientos Bancarios":
    st.subheader("🏦 Procesamiento de movimientos bancarios")
    st.write(
        """
        Procesa archivos PDF bancarios:
        ✔ Extracción de movimientos  
        ✔ Limpieza de datos  
        ✔ Clasificación  
        ✔ Validaciones  
        ✔ Carga PostgreSQL
        """
    )

    if st.button("▶ Procesar Banco"):
        with st.spinner("Procesando movimientos bancarios..."):
            pipeline_movBancarios()
        st.success(
            f"Proceso finalizado correctamente "
            f"({datetime.now().strftime('%d/%m/%Y %H:%M')})")
# Facturas

elif opcion == "Facturas":
    st.subheader("Procesamiento de facturas")
    st.write(
        """
        Procesa archivos Excel:

        ✔ Facturas recibidas  
        ✔ Facturas emitidas  
        ✔ Normalización de datos  
        ✔ Validaciones de calidad  
        ✔ Carga PostgreSQL
        """)
    if st.button("▶ Procesar Facturas"):
        with st.spinner("Procesando facturas..."):
            pipeline_facturas()
        st.success(
            f"Proceso finalizado correctamente "
            f"({datetime.now().strftime('%d/%m/%Y %H:%M')})")


# Todo

elif opcion == "Ejecutar Todo":
    st.subheader("🚀 Ejecución completa")
    if st.button("▶ Ejecutar Pipeline Completo"):
        progreso = st.progress(0)
        with st.spinner("Ejecutando procesos..."):
            pipeline_movBancarios()
            progreso.progress(50)
            pipeline_facturas()
            progreso.progress(100)
        st.success("Todos los procesos finalizaron correctamente.")