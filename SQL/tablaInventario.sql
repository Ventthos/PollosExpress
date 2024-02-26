USE u119126_pollos2LaVengazaDelPollo;

# SHOW TABLES;
DROP TABLE IF EXISTS inventario;

SELECT * FROM producto;

CREATE TABLE inventario (
    id_producto INT NOT NULL,
    nombre_producto NVARCHAR(100) NOT NULL,
    unidad VARCHAR(3) NOT NULL,
    cantidad INT NOT NULL,
    estado BOOLEAN NOT NULL,
    PRIMARY KEY(id_producto),
    FOREIGN KEY(id_producto) REFERENCES producto(id_producto)
);

#INSERT INTO inventario (id_producto, nombre_producto, unidad, cantidad, estado) VALUES (20, 'Mollo con pole', 'KG', 10, 0);
#INSERT INTO inventario (id_producto, nombre_producto, unidad, cantidad, estado) VALUES (31, 'Pollo asado', 'KG', 20, TRUE);
#INSERT INTO inventario (id_producto, nombre_producto, unidad, cantidad, estado) VALUES (34, 'Hace algo', '--', 20, TRUE);
#INSERT INTO inventario (id_producto, nombre_producto, unidad, cantidad, estado) VALUES (35, 'Nuevo producto', '--', 0, TRUE);
#INSERT INTO inventario (id_producto, nombre_producto, unidad, cantidad, estado) VALUES (36, 'Prueba', '--', 0, TRUE);
INSERT INTO inventario (id_producto, nombre_producto, unidad, cantidad, estado) VALUES (47, 'Yopo asado', '--', 0, FALSE);
INSERT INTO inventario (id_producto, nombre_producto, unidad, cantidad, estado) VALUES (50, 'Poyo', '--', 0, TRUE);

SELECT * FROM inventario;
