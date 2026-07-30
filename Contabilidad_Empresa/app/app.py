#Librerias
import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path
import sys

#Setear las rutas
ROOT_DIR = Path(__file__).resolve().parent.parent # resolve obtiene la ruta absoluta
sys.path.append(str(ROOT_DIR))
img_path = ROOT_DIR / "img" 
#FUnciones de mis propios archivos
from src.pipeline_movBancarios import pipeline_movBancarios
from src.pipeline_facturas import pipeline_facturas
from src.conexion import engine

#Funcion para traer los estilos del css
def cargar_css():
    ruta_css = Path(__file__).parent / "style.css"
    with open(ruta_css) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Configuración
st.set_page_config(page_title="Contabilidad",page_icon="📊",layout="wide")

#Se carga el css que esta en el otro archivo
cargar_css()

# Titulo
# st.title("Sistema de Gestión Contable")
# st.caption("Pipeline ETL - Extracción, Transformación, Validación y Carga")
# st.image(img_path / "logo.png", width=80)
# st.divider()


# Header con logo y título

col_logo, col_titulo = st.columns([0.5, 4])

with col_logo:
    st.image(img_path / "logo.png", width=80)

with col_titulo:
    st.title("Sistema de Gestión Contable")
    st.caption("Pipeline ETL - Extracción, Transformación, Validación y Carga")

st.divider()


# SIDEBAR
st.sidebar.title("Procesamiento")

opcion = st.sidebar.radio(
   "Seleccionar proceso",
   ["Resumen","Movimientos Bancarios","Facturas", "Ejecutar Todo"])

# opcion = st.selectbox("Resumen","Movimientos Bancarios","Facturas", "Ejecutar Todo")

# RESUMEN
if opcion == "Resumen":
    # st.subheader("Resumen del sistema")
    st.markdown("""<div class="titulos_generales_seccion"> Resumen del sistema </div> """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    # with col1:
    #     st.metric( "Estado ETL", "Listo")

    with col1:
        #st.metric("Estado ETL", "🟢 Operativo")
        st.markdown("""<div class="card">
        <div class="card-title">Estado ETL</div>
        <div class="card-value">🟢 Operativo</div>
        </div> """, unsafe_allow_html=True)

    with col2:
        #st.metric("Motor BD", "PostgreSQL")
        st.markdown("""<div class="card">
        <div class="card-title">Motor BD</div>
        <div class="card-value">PostgreSQL</div>
        </div> """, unsafe_allow_html=True)

    with col3:
        #st.metric("Última ejecución", datetime.now().strftime("%d/%m/%Y"))
        st.markdown(f"""<div class="card">
        <div class="card-title">Última ejecución</div>
        <div class="card-value">{datetime.now().strftime("%d/%m/%Y")}</div>
    </div>
    """, unsafe_allow_html=True)


    # st.divider()
    #st.subheader("Información disponible")
    # st.markdown("""<div class="titulos_generales_seccion"> Información disponible </div> """, unsafe_allow_html=True)
    st.markdown("""<div class="subseccion">Información disponible</div>""",unsafe_allow_html=True)
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
            # st.markdown("### Movimientos Bancarios")
            # st.markdown('<div class="titulo-card">Movimientos Bancarios</div>', unsafe_allow_html=True)
            # st.metric("Registros",int(banco["registros"].iloc[0]))
            st.markdown(f"""<div class="card">
            <div class="card-title">Movimientos Bancarios</div>
            <div class="card-value">{int(banco["registros"].iloc[0])}</div>
            </div> """, unsafe_allow_html=True)
            if banco["desde"].iloc[0]:
                # st.write(
                #     f"""
                #     Periodo: {banco["desde"].iloc[0].strftime('%d/%m/%Y')} - {banco["hasta"].iloc[0].strftime('%d/%m/%Y')}
                #     """)
                st.markdown(f"""<div class="periodo-card">
                Periodo: {banco["desde"].iloc[0].strftime('%d/%m/%Y')} -{banco["hasta"].iloc[0].strftime('%d/%m/%Y')}
                </div> """, unsafe_allow_html=True)
        with col2:
            #st.markdown("### Facturas Recibidas")
            # st.markdown('<div class="titulo-card">Facturas Recibidas</div>', unsafe_allow_html=True)
            # st.metric("Registros",int(compras["registros"].iloc[0]))
            st.markdown(f"""<div class="card">
                        <div class="card-title">Facturas Recibidas</div>
                        <div class="card-value">{int(compras["registros"].iloc[0])}</div>
                        </div> """, unsafe_allow_html=True)
            if compras["desde"].iloc[0]:
                # st.write(f"""Periodo: {compras["desde"].iloc[0].strftime('%d/%m/%Y')} - {compras["hasta"].iloc[0].strftime('%d/%m/%Y')}""")
                st.markdown(f"""<div class="periodo-card">
                                Periodo: {compras["desde"].iloc[0].strftime('%d/%m/%Y')} -{compras["hasta"].iloc[0].strftime('%d/%m/%Y')}
                                </div> """, unsafe_allow_html=True)
                
        with col3:
            # st.markdown("### Facturas Emitidas")
            # st.markdown('<div class="titulo-card">Facturas Emitidas</div>', unsafe_allow_html=True)
            # st.metric( "Registros", int(ventas["registros"].iloc[0]))
            st.markdown(f"""<div class="card">
            <div class="card-title">Facturas Emitidas</div>
            <div class="card-value">{int(ventas["registros"].iloc[0])}</div>
            </div> """, unsafe_allow_html=True)

            if ventas["desde"].iloc[0]:
                # st.write( f""" Periodo: {ventas["desde"].iloc[0].strftime('%d/%m/%Y')} - {ventas["hasta"].iloc[0].strftime('%d/%m/%Y')} """)
                st.markdown(f"""<div class="periodo-card">
                Periodo: {ventas["desde"].iloc[0].strftime('%d/%m/%Y')} -{ventas["hasta"].iloc[0].strftime('%d/%m/%Y')}
                </div> """, unsafe_allow_html=True)
        st.divider()
        st.info(
            """
            El sistema contiene información procesada desde:
            - Extractos bancarios PDF
            - Facturas de compra (recibidas)
            - Facturas de venta (emitidas)
            - Los datos fueron extraídos, transformados, validados y cargados en PostgreSQL.
            """
        )

    except Exception as e:
        st.warning(f"No fue posible consultar la información disponible: {e}")

#Banco


elif opcion == "Movimientos Bancarios":
    st.subheader("Procesamiento de movimientos bancarios")
    st.write(
        """
        Procesa archivos PDF bancarios:
        ✔ Extracción de movimientos  
        ✔ Limpieza de datos  
        ✔ Clasificación  
        ✔ Validaciones  
        ✔ Carga PostgreSQL
        """)

    if st.button("Procesar Banco"):
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
    if st.button("Procesar Facturas"):
        with st.spinner("Procesando facturas..."):
            pipeline_facturas()
        st.success(
            f"Proceso finalizado correctamente "
            f"({datetime.now().strftime('%d/%m/%Y %H:%M')})")
    # Todo

elif opcion == "Ejecutar Todo":
    st.subheader(" Ejecución completa")
    if st.button("Ejecutar Pipeline Completo"):
        progreso = st.progress(0)
        with st.spinner("Ejecutando procesos..."):
            pipeline_movBancarios()
            progreso.progress(50)
            pipeline_facturas()
            progreso.progress(100)
        st.success("Todos los procesos finalizaron correctamente.")




# /* Nombre de la métrica */
# label[data-testid="stMetricLabel"]{
#     justify-content:center;
# }

# label[data-testid="stMetricLabel"] div[data-testid="stMarkdownContainer"] p{
#     font-size:15px !important;
#     font-weight:700 !important;
#     color:#555555 !important;
#     text-align:center !important;
#     margin:0 !important;
# }

# /* Valor de la métrica */
# div[data-testid="stMetricValue"]{
#     font-size:16px !important;
#     font-weight:600 !important;
#     color:#31a354;
#     text-align: center;
# }