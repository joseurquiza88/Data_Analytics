-- Crear base y despues setearla con posgress a nivel local
CREATE DATABASE contabilidad;

-- Confirmar que realmente estamos dentro de contabilidad
SELECT current_database();

-- Esta ok
SELECT current_user;

-- Crear tablas
-- Info de las tablas generadas
CREATE TABLE archivos_procesados (
    id SERIAL PRIMARY KEY,
    nombre_archivo TEXT UNIQUE NOT NULL,
    fecha_procesamiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cantidad_registros INTEGER,
    estado TEXT, -- responde: que paso con el procesamiento?
    error TEXT, -- responde: si salio mal, porque fue?
    tipo_archivo TEXT
);


-- Tabla de movimientos bancariso
CREATE TABLE movimientos_bancarios (
    id SERIAL PRIMARY KEY,
    fecha DATE,
    comprobante TEXT,
    movimiento TEXT,
    debito NUMERIC(15,2),
    credito NUMERIC(15,2),
    saldo_en_cuenta NUMERIC(15,2),
    mes TEXT,
    categoria TEXT,
    archivo_origen TEXT NOT NULL,
    fecha_carga TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Probando...
-- DROP TABLE archivos_procesados;
-- DROP TABLE movimientos_bancarios;

SELECT * FROM archivos_procesados;
SELECT
    column_name,
    data_type
FROM information_schema.columns
WHERE table_name = 'movimientos_bancarios';

-- Para hacer pruebas
DELETE FROM movimientos_bancarios
WHERE EXTRACT(YEAR FROM fecha) = 2026;

DELETE FROM movimientos_bancarios
WHERE archivo_origen = '01-2026_banco.pdf'


SELECT MIN(mes) AS mes_inicio, MAX(mes) AS mes_fin
FROM movimientos_bancarios

SELECT COUNT(*) 
FROM movimientos_bancarios;

SELECT DISTINCT archivo_origen
FROM movimientos_bancarios;

SELECT current_database();

SELECT *
FROM movimientos_bancarios
ORDER BY fecha_carga DESC
LIMIT 10;

SELECT mes, COUNT(*) AS cantidad_movimientos
FROM movimientos_bancarios
GROUP BY mes
ORDER BY mes;

SELECT COUNT(*) 
FROM movimientos_bancarios
WHERE fecha IS NULL;

SELECT COUNT(*)
FROM movimientos_bancarios;

-- ####################################################
-- FACTURA EMITIDAS Y RECIBIDAS

CREATE TABLE fact_recibidas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    mes TEXT NOT NULL,
    tipo_comprobante TEXT NOT NULL,
    punto_venta TEXT NOT NULL,
    numero_comprobante TEXT NOT NULL,
    razon_social TEXT NOT NULL,
    cuit TEXT,
    condicion TEXT NOT NULL,
    concepto TEXT NOT NULL,
    forma_pago TEXT NOT NULL,

    neto_gravado NUMERIC(15,2) NOT NULL,
    iva_10_5 NUMERIC(15,2) DEFAULT 0,
    iva_21 NUMERIC(15,2) NOT NULL,
    iva_27 NUMERIC(15,2) DEFAULT 0,
    iva_3 NUMERIC(15,2) DEFAULT 0,
    percepcion_iibb NUMERIC(15,2) DEFAULT 0,
    percepcion_municipal NUMERIC(15,2) DEFAULT 0,
    no_gravado_exento NUMERIC(15,2) DEFAULT 0,
    total NUMERIC(15,2) NOT NULL,

    fecha_procesamiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    archivo_origen TEXT NOT NULL
);

CREATE TABLE fact_emitidas (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    mes TEXT NOT NULL,
    tipo_comprobante TEXT NOT NULL,
    punto_venta TEXT NOT NULL,
    numero_comprobante TEXT NOT NULL,
    razon_social TEXT NOT NULL,
    cuit TEXT,
    forma_cobro TEXT NOT NULL,

    neto_gravado NUMERIC(15,2) NOT NULL,
    iva_10_5 NUMERIC(15,2) DEFAULT 0,
    iva_21 NUMERIC(15,2) NOT NULL,
    iva_27 NUMERIC(15,2) DEFAULT 0,
    iva_3 NUMERIC(15,2) DEFAULT 0,
    percepcion_iibb NUMERIC(15,2) DEFAULT 0,
    percepcion_municipal NUMERIC(15,2) DEFAULT 0,
    no_gravado_exento NUMERIC(15,2) DEFAULT 0,
    total NUMERIC(15,2) NOT NULL,

    fecha_procesamiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    archivo_origen TEXT NOT NULL
);

drop table fact_emitidas;
drop table fact_recibidas;

DELETE FROM fact_recibidas
WHERE EXTRACT(YEAR FROM fecha) = 2026;
DELETE FROM fact_emitidas
WHERE EXTRACT(YEAR FROM fecha) = 2026;



-- ####################################################
-- Productos vendidos

CREATE TABLE detalle_fact_emitidas (
    id SERIAL PRIMARY KEY,
    cliente_doc TEXT,
    fecha_venta DATE NOT NULL,
    mes TEXT NOT NULL,
    punto_venta TEXT NOT NULL,
    comp_nro TEXT NOT NULL,
    razon_social TEXT,
    condicion_iva TEXT,
    domicilio TEXT,
    condicion_venta TEXT NOT NULL,
    producto TEXT NOT NULL,
    cantidad NUMERIC DEFAULT 0,
    unidad TEXT,
    precio_unitario NUMERIC(15,2) DEFAULT 0,
    bonificacion NUMERIC(15,2) DEFAULT 0,
    importe_bonificacion NUMERIC(15,2) DEFAULT 0,
    subtotal NUMERIC(15,2) DEFAULT 0,
    fecha_procesamiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    archivo_origen TEXT NOT NULL
);
drop table productos_vendidos;
SELECT * FROM detalle_fact_emitidas;

SELECT * FROM detalle_fact_emitidas;
DELETE FROM detalle_fact_emitidas
WHERE fecha_venta >= '2026-07-01'
AND fecha_venta < '2026-08-01';