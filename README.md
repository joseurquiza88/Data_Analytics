![Banner del proyecto](/Contabilidad_Empresa/img/banner_finanzas.png)

## 📌 Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de integración, procesamiento y análisis de información contable de una empresa.

El objetivo principal es transformar información dispersa y en diferentes formatos (imágenes, archivos PDF y registros contables) en datos estructurados, centralizados y disponibles para análisis.

La solución implementa un flujo completo de datos (**ETL - Extract, Transform, Load**) que permite automatizar tareas manuales, mejorar la calidad de la información y facilitar la toma de decisiones basada en datos.

---

## 🎯 Objetivos del proyecto

- Extraer información desde diferentes fuentes de datos.
- Automatizar la lectura de tickets mediante técnicas de OCR que provienen de fotos
- Extraer movimientos bancarios desde documentos PDFs.
- Procesar y limpiar información utilizando Python.
- Diseñar un modelo de datos relacional.
- Centralizar la información en una base de datos PostgreSQL.
- Realizar análisis mediante consultas SQL.
- Construir dashboards interactivos para seguimiento financiero.
- Desarrollar una aplicación web para consulta y procesamiento de información.

---

# 🏗️ Arquitectura del sistema

![Arquitectura del pipeline](images/arquitectura_pipeline.png)

El flujo general del proyecto es:

```text
Fuentes de información
        │
        │
        ▼
Extracción de datos
(OCR (imagenes/fotos) / PDF Parsing / Archivos contables (.xls))
        │
        ▼
Procesamiento y transformación
(Python - Pandas)
        │
        ▼
Validación y limpieza
        │
        ▼
Base de datos PostgreSQL
        │
        ├──────────────► Consultas analíticas SQL
        │
        ├──────────────► Dashboards Power BI
        │
        └──────────────► Aplicación Streamlit
```

---

# 📂 Fuentes de información

El sistema integra información proveniente de diferentes fuentes:

### 🧾 Tickets

Documentos en formato imagen procesados mediante técnicas de OCR para extraer información como:

- Fecha.
- Número de comprobante.
- Razón social.
- CUIT.
- Importes.
- Impuestos.
- Total de la operación.

---

### 🏦 Resúmenes bancarios

Archivos PDF procesados para obtener información de movimientos:

- Fecha.
- Comprobante.
- Descripción del movimiento.
- Débitos.
- Créditos.
- Saldo disponible.

---

### 📑 Información contable

Registros financieros utilizados para complementar el análisis y generar indicadores de seguimiento.

---
# 📁 Estructura del proyecto

```text
contabilidad_empresa/

├── app/
│   ├── app.py             # app de streamlit
│   └── style.css          # Estilos
│
├── data/
│   ├── raw/                # Datos originales
│   └── processed/          # Datos procesados
│ 
├── img/
│
├── notebooks/
│   ├── analisis_movimientos_bancarios.ipynb      
│   ├── contabilidad_mensual.ipynb      
│   ├── estructuracion_base_datos.ipynb     
│   ├── movimientos_bancarios.ipynb     
│   ├── prueba_pipeline.ipynb    
│   └── ticketss.ipynb
│
├── PowerBI/
│   └── Insight_relevantes.pbix
│
├── sql/
│   └── schema.sql
├── src/
│   ├── conexion.py         # Extracción de información
│   ├── extract.py          # Extracción de información
│   ├── load.py             # Carga a PostgreSQL
│   ├── main.py             # archivo principal del pipeline completo
│   ├── pipeline_facturas.py          
│   ├── pipeline_movBancarios.py          
│   ├── test.py             # Testeos previo a la carga
│   └── transform.py        # Transformacion de datos
│
└── README.md
```
---
# 🛠️ Tecnologías utilizadas

## Lenguajes

- Python
- SQL

## Procesamiento y análisis de datos

- Pandas
- NumPy

## Extracción de información

- OpenCV
- Tesseract OCR
- pdfplumber

## Base de datos

- PostgreSQL

## Visualización

- Power BI
- Streamlit

## Desarrollo

- Git
- GitHub

---

## Ejemplo de dashboard

![Dashboard financiero](/Contabilidad_Empresa/img/app-streamlit.JPG)

---

#### 🚧 Estado del proyecto

Actualmente el proyecto se encuentra en desarrollo.

#### 📌 Próximamente

Este proyecto continuará evolucionando hacia una solución completa de analítica financiera, incorporando automatización, mejores prácticas de ingeniería de datos y herramientas de visualización para soporte a la toma de decisiones.
