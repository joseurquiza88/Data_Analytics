
import streamlit as st
import pandas as pd
from datetime import datetime

from src.pipeline_movBancarios import pipeline_movBancarios
from src.pipeline_facturas import pipeline_facturas
from src.conexion import engine


# Configuración
st.set_page_config(page_title="Contabilidad",page_icon="📊",layout="wide")
st.markdown("""
<style>

/* Tarjetas de métricas */
div[data-testid="stMetric"]{
    background-color:#ffffff;
    border:1px solid #DCE3EC;
    border-radius:14px;
    padding:15px;
    text-align: center;
    box-shadow:0 3px 8px rgba(0,0,0,0.08);
}

.card{
    background:white;
    border:1px solid #DCE3EC;
    border-radius:14px;
    padding:16px;
    text-align:center;
    box-shadow:0 3px 8px rgba(0,0,0,0.08);
}

.card-title{
    font-size:14px;
    font-weight:600;
    color:#6b7280;
    margin-bottom:10px;
}

.card-value{
    font-size:16px;
    font-weight:700;
    color:#1f2937;
}

/* Títulos de sección */
.titulos_generales_seccion{
    font-size:22px;
    font-weight:700;
    color:#1f2937;
    letter-spacing:-0.3px;
    margin:12px 0 18px 0;
    
}

.titulo-card{
    font-size:18px;
    font-weight:700;
    color:#1f2937;
    justify-content: space-between;
    margin-bottom:8px;
}

.periodo-card{
    font-size:12px;
    font-weight:400;
    color:#6b7280;
    margin-top:10px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)



# Titulo
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


    st.divider()
    #st.subheader("Información disponible")
    # st.markdown("""<h2 id="info-disponible"> Información disponible </h2>""", unsafe_allow_html=True), no funciono!
    st.markdown("""<div class="titulos_generales_seccion"> Información disponible </div> """, unsafe_allow_html=True)
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