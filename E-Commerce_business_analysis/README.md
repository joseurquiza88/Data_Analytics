


# E-commerce Customer Behavior & Sales Analysis

## 📌 Descripción del proyecto

Análisis exploratorio de datos de un e-commerce para comprender el comportamiento de compra de los clientes, identificar patrones de facturación y explorar qué factores podrían estar relacionados con la recompra.

El trabajo combina consultas SQL para explorar y analizar los datos con Python en Jupyter Notebook para realizar análisis estadísticos, visualizaciones y una exploración inicial de modelos predictivos.

## 🎯 Objetivo del análisis

Investigar la relación entre las características de los clientes, su comportamiento de compra, la experiencia digital y las variables posteriores a la compra, con foco en dos aspectos principales:

- **Ingresos:** ¿qué categorías, precios y características de las compras concentran la facturación?
- **Recompra:** ¿qué variables muestran una posible relación con la recurrencia de los clientes?

## 📊 Dataset

Los datos provienen de un conjunto de datos público de Kaggle sobre comportamiento de clientes y ventas en e-commerce.

🔗 [E-commerce Customer Behavior and Sales Analysis – Kaggle](https://www.kaggle.com/datasets/umuttuygurr/e-commerce-customer-behavior-and-sales-analysis-tr)

El dataset incluye información sobre transacciones, perfil de clientes, productos, navegación digital, métodos de pago y experiencia posterior a la compra.

### Variables analizadas

| Dimensión | Variables principales |
|---|---|
| Perfil del cliente | Age, Gender, City |
| Compras e ingresos | Product_Category, Unit_Price, Quantity, Discount_Amount, Total_Amount |
| Comportamiento digital | Device_Type, Session_Duration_Minutes, Pages_Viewed |
| Experiencia post-compra | Delivery_Time_Days, Customer_Rating |
| Recurrencia | Customer_ID, Order_ID, Is_Returning_Customer |

## 🔎 Preguntas de negocio

### 1. Perfil de los clientes
- ¿Cómo se distribuyen los clientes por edad, género y ciudad?
- ¿Qué ciudades concentran la mayor cantidad de órdenes?
- ¿Existen diferencias relevantes entre segmentos de clientes?

### 2. Comportamiento de compra e ingresos
- ¿Qué categorías generan mayor facturación?
- ¿Cómo se relacionan el precio unitario y la cantidad comprada con el importe total?
- ¿Qué proporción de las compras recibe descuentos?
- ¿Cómo se distribuyen los ingresos entre las órdenes?
- ¿Qué categorías presentan precios y tickets más elevados?

### 3. Comportamiento digital
- ¿Qué dispositivos se utilizan con mayor frecuencia para comprar?
- ¿Cuánto tiempo permanecen los clientes en el sitio antes de comprar?
- ¿Existe alguna relación entre las páginas visitadas, la duración de la sesión y el importe de la compra?

### 4. Experiencia y recompra
- ¿Qué proporción de las órdenes corresponde a clientes recurrentes?
- ¿Cómo se relacionan los tiempos de entrega y las calificaciones con la recurrencia?
- ¿Se observan diferencias entre clientes recurrentes y no recurrentes?

## 🛠️ Metodología

1. **Exploración con SQL:** consultas para revisar la estructura de los datos, analizar distribuciones, agrupar resultados y responder preguntas sobre ventas y clientes.
2. **Preparación y validación:** revisión de valores nulos, registros duplicados, tipos de datos y consistencia de las variables.
3. **Análisis exploratorio con Python:** estadística descriptiva, análisis de distribuciones, comparación entre segmentos y visualización de patrones.
4. **Análisis de recompra:** exploración de asociaciones entre las variables disponibles y evaluación inicial de un modelo de clasificación.
5. **Interpretación:** síntesis de los principales hallazgos y de las limitaciones de los datos para responder las preguntas planteadas.

## 📈 Principales hallazgos

### Perfil del cliente
- La edad promedio se sitúa alrededor de los 35 años, con concentración entre los 26 y 42 años.
- La distribución por género es relativamente equilibrada.
- El dataset incluye clientes de 10 ciudades, con una concentración importante de órdenes en Estambul.

### Comportamiento de compra
- El volumen de órdenes se distribuye de manera relativamente equilibrada entre las categorías.
- Electronics presenta precios unitarios superiores a los de las demás categorías.
- La mitad de las órdenes no registra descuentos.
- La facturación presenta una distribución asimétrica: una proporción reducida de compras de alto valor concentra una parte importante de los ingresos.
- El precio unitario parece tener mayor relevancia para explicar las diferencias de facturación que la cantidad comprada por sí sola.

### Comportamiento digital
- El dispositivo móvil concentra aproximadamente el 56 % de las órdenes, seguido por Desktop, con cerca del 34 %.
- La duración media de las sesiones es de aproximadamente 14,5 minutos y el promedio de páginas vistas es cercano a 9.

### Experiencia post-compra y recurrencia
- El tiempo medio de entrega es de aproximadamente 6,5 días.
- La calificación media de los clientes se sitúa alrededor de 3,9 sobre 5.
- Cerca del 88 % de las órdenes está asociado a clientes identificados como recurrentes según la variable disponible.

## 🧪 Exploración de la recompra

Se realizó una exploración inicial para evaluar si las variables disponibles permitían distinguir a los clientes recurrentes de los no recurrentes.

Los resultados mostraron un fuerte desbalance en la variable objetivo: aproximadamente el 88 % de las observaciones corresponde a la clase recurrente. En este contexto, un modelo puede alcanzar una accuracy elevada simplemente prediciendo la clase mayoritaria, sin identificar adecuadamente a los clientes no recurrentes.

El análisis inicial no permitió identificar relaciones suficientemente claras para distinguir ambas clases. Por lo tanto, los resultados no permiten concluir que estas variables carezcan de relación con la recompra, sino que el enfoque utilizado y la información disponible no fueron suficientes para establecer patrones predictivos sólidos.

## 💡 Conclusiones

- La facturación está fuertemente influenciada por las compras de alto valor y las diferencias de precio entre categorías.
- La distribución de los ingresos requiere analizar tanto el ticket promedio como el volumen de órdenes y unidades vendidas.
- El predominio de clientes recurrentes genera un desafío metodológico para estudiar la recompra mediante modelos de clasificación.
- Para profundizar el análisis, sería útil contar con información temporal más detallada del historial de cada cliente y definir la recompra dentro de un período específico.

## 🧰 Tecnologías utilizadas

- **SQL:** consultas, agregaciones y análisis de datos.
- **Python:** procesamiento y análisis exploratorio.
- **Jupyter Notebook:** desarrollo y documentación del análisis.
- **Pandas y NumPy:** manipulación de datos.
- **Matplotlib y Seaborn:** visualización de resultados.
- **Scikit-learn:** exploración inicial de modelos de clasificación.

## 📁 Estructura del proyecto

```text
ecommerce-customer-analysis/
├── notebooks/
│   └── analisis_exploratorio.ipynb
├── sql/
│   └── consultas.sql
├── README.md
└── ...
```

*La estructura es ilustrativa y debe adaptarse a los archivos reales del repositorio.*

## 📌 Alcance y limitaciones

Este proyecto tiene un enfoque exploratorio y utiliza un dataset público. Los patrones observados describen los datos disponibles y no demuestran causalidad. Los resultados del análisis de recompra están condicionados por el desbalance de clases y por las variables incluidas en el conjunto de datos.
