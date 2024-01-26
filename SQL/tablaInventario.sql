USE u119126_pollos2LaVengazaDelPollo;

# SHOW TABLES;
DROP TABLE IF EXISTS inventario;

SELECT * FROM producto;

CREATE TABLE inventario (
    id_producto INT NOT NULL,
    nombre_producto VARCHAR(100) NOT NULL,
    unidad VARCHAR(3) NOT NULL,
    cantidad INT NOT NULL,
    PRIMARY KEY(id_producto),
    FOREIGN KEY(id_producto) REFERENCES producto(id_producto)
);
# ALTER TABLE u119126_pollos2LaVengazaDelPollo.inventario MODIFY COLUMN cantidad INT NOT NULL;

INSERT INTO inventario (id_producto, nombre_producto, unidad, cantidad) VALUES (20, 'Mollo con pole', 'KG', 10);

SELECT * FROM inventario;