# E-Commerce Returns Analysis

## 📌 Descripción

Las devoluciones representan un costo importante para las empresas de comercio electrónico, tanto por los gastos logísticos como por los costos asociados a la gestión de los productos devueltos.

Este proyecto analiza un dataset de transacciones de e-commerce con el objetivo de identificar qué características de los clientes, productos y pedidos están asociadas con una mayor probabilidad de devolución.

El análisis sigue un flujo de trabajo orientado a un caso de negocio real, combinando análisis exploratorio en Python, consultas SQL y visualización de resultados mediante Power BI.

---

## 🎯 Problema de negocio

Una empresa de comercio electrónico busca reducir la cantidad de productos devueltos, pero no conoce con claridad cuáles son los factores que están asociados a las devoluciones.

En lugar de asumir que las devoluciones se deben principalmente al precio, los descuentos o las características del producto, este análisis busca identificar patrones en los datos y determinar dónde debería concentrar sus esfuerzos la empresa.

### Pregunta principal

> **¿Qué factores están asociados a que una compra de e-commerce sea devuelta?**

### Preguntas secundarias

- ¿Qué categorías de productos presentan mayores tasas de devolución?
- ¿El tiempo de entrega influye en la probabilidad de devolución?
- ¿Los productos de mayor precio se devuelven con mayor frecuencia?
- ¿Los descuentos tienen relación con las devoluciones?
- ¿El rating del producto está asociado con la devolución?
- ¿El método de envío afecta la tasa de devolución?
- ¿Existen características de los clientes asociadas a una mayor tasa de devolución?
- ¿Qué factores representan las principales oportunidades de mejora para el negocio?

---

## 🎯 Objetivos

Los principales objetivos del proyecto son:

1. Comprender la estructura y calidad del dataset.
2. Explorar las características de clientes, productos y pedidos.
3. Identificar patrones asociados a las devoluciones.
4. Calcular y comparar tasas de devolución según diferentes variables.
5. Utilizar SQL para responder preguntas orientadas al negocio.
6. Desarrollar un dashboard interactivo en Power BI.
7. Transformar los hallazgos del análisis en recomendaciones de negocio.

---

## 📊 Dataset

**Dataset:** E-Commerce Returns: Who Will Send It Back?

El dataset contiene información a nivel de transacción que permite analizar si una compra online es devuelta a partir de características del cliente, del producto y del pedido.

La variable objetivo utilizada en el análisis es:

- `returned`: indica si la compra fue devuelta.

### Nota sobre los datos

El dataset es utilizado con fines educativos y de portfolio. El caso de negocio planteado es hipotético y no representa las operaciones ni los resultados reales de una empresa específica.

---

## 🔎 Metodología

El proyecto sigue las siguientes etapas:

### 1. Comprensión y calidad de los datos

En esta primera etapa se analiza la estructura general del dataset y su calidad.

Se revisan:

- Cantidad de registros y variables
- Tipos de datos
- Valores nulos
- Registros duplicados
- Valores únicos
- Estadísticas descriptivas
- Distribución de la variable objetivo
- Posibles inconsistencias en los datos

### 2. Análisis exploratorio — Python

Se utiliza Python para explorar las relaciones entre las devoluciones y las diferentes características disponibles en el dataset.

El análisis incluye comparaciones entre:

- Compras devueltas y no devueltas
- Categorías de productos
- Métodos de envío
- Tiempo de entrega
- Precio
- Descuentos
- Rating del producto
- Características y comportamiento de los clientes

El objetivo no es solamente describir los datos, sino identificar patrones que permitan responder las preguntas de negocio.

### 3. Análisis con SQL

SQL se utiliza para profundizar el análisis y responder preguntas de negocio mediante consultas estructuradas.

Entre los análisis realizados se encuentran:

- Tasa general de devolución
- Tasa de devolución por categoría
- Tasa de devolución por método de envío
- Tasa de devolución según tiempo de entrega
- Tasa de devolución según rango de precio
- Tasa de devolución según nivel de descuento
- Tasa de devolución por segmento de cliente
- Comparación entre pedidos devueltos y no devueltos

### 4. Visualización — Power BI

Los principales hallazgos se trasladan a un dashboard interactivo en Power BI.

El dashboard permitirá analizar:

- Evolución y nivel general de las devoluciones
- Tasa de devolución por categoría
- Relación entre tiempo de entrega y devoluciones
- Comportamiento según método de envío
- Características de los pedidos devueltos
- Principales factores asociados a las devoluciones

---

## 📈 Principales métricas

Las principales métricas consideradas en el análisis son:

- Total de pedidos
- Pedidos devueltos
- Tasa de devolución
- Valor promedio del pedido
- Tiempo promedio de entrega
- Descuento promedio
- Rating promedio del producto

Se incorporarán métricas adicionales a medida que avance el análisis y se identifiquen nuevas necesidades de negocio.

---

## 💡 Principales hallazgos

> **Esta sección se completará una vez finalizado el análisis exploratorio y las consultas SQL.**

El análisis buscará identificar qué variables presentan las mayores diferencias entre los pedidos devueltos y los pedidos no devueltos.

Entre los aspectos analizados se encuentran:

- Influencia del tiempo de entrega.
- Diferencias entre categorías de productos.
- Relación entre descuentos y devoluciones.
- Relación entre rating y devoluciones.
- Influencia del precio.
- Características de los clientes con mayor tasa de devolución.

Los hallazgos finales estarán basados en los patrones observados en los datos y no en hipótesis previamente asumidas.

---

## 🏢 Recomendaciones de negocio

> **Esta sección se completará una vez finalizado el análisis.**

A partir de los principales hallazgos se desarrollarán recomendaciones orientadas a:

- Optimizar procesos logísticos y tiempos de entrega.
- Identificar categorías con mayores niveles de devolución.
- Mejorar la experiencia del cliente.
- Revisar estrategias de envío.
- Detectar posibles problemas relacionados con determinados productos.
- Implementar estrategias para reducir devoluciones evitables.

Las recomendaciones estarán fundamentadas en la evidencia encontrada en los datos.

---

## 🛠️ Herramientas utilizadas

- **Python** — Limpieza, transformación y análisis exploratorio
- **Pandas** — Manipulación de datos
- **NumPy** — Análisis numérico
- **Matplotlib / Seaborn** — Visualización
- **SQL** — Exploración y análisis orientado al negocio
- **Power BI** — Dashboard y visualización interactiva
- **Git & GitHub** — Control de versiones y documentación

---

## 📁 Estructura del proyecto

```text
ecommerce-returns-analysis/
│
├── README.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── sql/
│   ├── 01_data_quality.sql
│   ├── 02_exploration.sql
│   └── 03_business_analysis.sql
│
├── powerbi/
│   └── ecommerce_returns.pbix
│
└── reports/
    └── figures/
