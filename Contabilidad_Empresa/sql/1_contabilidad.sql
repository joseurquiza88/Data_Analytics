CREATE DATABASE contabilidad;
-- Crear tabla
CREATE TABLE archivos_procesados (
    id SERIAL PRIMARY KEY,
    nombre_archivo TEXT UNIQUE NOT NULL,
    fecha_procesamiento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    cantidad_registros INTEGER,
    estado TEXT
);

CREATE TABLE movimientos_bancarios (
    id SERIAL PRIMARY KEY,
    fecha DATE,
    comprobante TEXT,
    movimiento TEXT,
    debito NUMERIC(15, 2),
    credito NUMERIC(15, 2),
    saldo_en_cuenta NUMERIC(15, 2),
    archivo_origen TEXT NOT NULL,
    fecha_carga TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM archivos_procesados;
SELECT
    column_name,
    data_type
FROM information_schema.columns
WHERE table_name = 'movimientos_bancarios';