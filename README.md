# 📊 Sistema de Integración y Análisis de Información Financiera

Este proyecto tiene como objetivo desarrollar un sistema para integrar, procesar y analizar información financiera y contable de una empresa.

### 🎯 Objetivos particulares

- Extraer información desde diferentes fuentes.
- Procesar y limpiar los datos utilizando Python.
- Automatizar la lectura de facturas, tickets y resúmenes bancarios.
- Centralizar la información en una base de datos.
- Integrar y relacionar datos financieros.
- Analizar la información mediante SQL.
- Crear dashboards interactivos en Power BI.

### 📂 Fuentes de información

- 🧾 Facturas y tickets en imágenes.
- 🏦 Resúmenes bancarios en PDF.
- 📑 Información contable.

El objetivo es transformar esta información dispersa en datos estructurados, centralizados y analizables.

```text
Facturas / Tickets ──┐
                     │
Resúmenes bancarios ─┼──► Python / ETL ──► PostgreSQL ──► Power BI
                     │
Datos contables ─────┘
```

### 🔄 Flujo del proyecto

```text
Fuentes de información
        ↓
Extracción
        ↓
Limpieza y transformación
        ↓
Validación
        ↓
Base de datos
        ↓
Análisis
        ↓
Power BI
```

---

### 🛠️ Tecnologías

- Python
- Pandas
- OpenCV
- Tesseract OCR
- pdfplumber
- SQL
- PostgreSQL
- Power BI
- Git / GitHub

### 📌 Estado del proyecto

🚧 **En desarrollo**

Actualmente se están desarrollando los procesos de:

- Extracción de información desde facturas y tickets mediante OCR.
- Extracción de movimientos desde resúmenes bancarios en PDF.
- Integración de información contable.
- Diseño de la base de datos central.
- Desarrollo de dashboards en Power BI.
