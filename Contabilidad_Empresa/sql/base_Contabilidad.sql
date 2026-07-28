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


