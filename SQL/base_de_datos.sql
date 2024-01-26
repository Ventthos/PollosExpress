#Mostrar producto a la que referencia, datos de la promocion y tipo
#CREATE DATABASE pollosexpress;
USE pollosexpress;
#DROP TABLE IF EXISTS pago, rol, empleado, cliente, venta, producto, gasto, tipo_de_promocion, venta_producto, promocion, inventario;
CREATE TABLE pago (
    id_pago INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre NVARCHAR(50)
);
CREATE TABLE rol (
    id_rol INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL,
    CONSTRAINT UNIQUE(nombre)
);
CREATE TABLE empleado (
    id_empleado INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
	apellido_paterno NVARCHAR(50) NOT NULL,
    apellido_materno NVARCHAR(50) NOT NULL,
    celular VARCHAR(11) NOT NULL,
    sueldo DOUBLE NOT NULL,
    id_rol INT,
    pass NVARCHAR(30),
    FOREIGN KEY (id_rol) REFERENCES rol(id_Rol),
    CONSTRAINT UQcelular UNIQUE(celular)
);
ALTER TABLE empleado
ADD COLUMN administrator bool NOT NULL;

alter table empleado
add column activo char(1) default "V";

CREATE TABLE cliente (
    id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    celular VARCHAR(10) NOT NULL,
    direccion VARCHAR(150) NOT NULL
);

alter table cliente
add column activo char(1) default "V";

CREATE TABLE venta (
    id_Venta INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    fecha_De_Venta DATE NOT NULL,
    total_De_Compra DOUBLE NOT NULL,
    id_pago INT,
    id_empleado INT,
    FOREIGN KEY (id_pago) REFERENCES pago(id_Pago),
    FOREIGN KEY (id_empleado) REFERENCES empleado(id_Empleado),
    id_cliente INT,
    FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)
);


CREATE TABLE producto (
    id_producto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL,
    descripcion NVARCHAR(200) NOT NULL,
    precio DOUBLE NOT NULL,
    imagen text NOT NULL
);

alter table producto
add column activo char(1) default "V";

CREATE TABLE gasto (
    id_gasto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo NVARCHAR(50) NOT NULL,
    descripcion NVARCHAR(150) NOT NULL,
    monto DECIMAL NOT NULL,
    fecha DATETIME NOT NULL,
    id_empleado INT,
    FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado)
);


CREATE TABLE tipo_de_promocion (
    id_tipo_promocion INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    codigo VARCHAR(50) NOT NULL
);



CREATE TABLE venta_producto (
    id_venta_producto INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_venta INT,
    id_producto INT,
    cantidad INT NOT NULL,
    subtotal DECIMAL,
    FOREIGN KEY (id_venta) REFERENCES venta(id_venta),
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);


CREATE TABLE promocion (
    id_promocion INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_producto INT,
    descripcion VARCHAR(200) NOT NULL,
    fecha_de_inicio DATE NOT NULL,
    fecha_de_finalizacion DATE,
    id_tipo_promocion INT,
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto),
    FOREIGN KEY (id_tipo_promocion) REFERENCES tipo_de_promocion(id_tipo_promocion),
    CONSTRAINT fecha_valida CHECK (fecha_de_inicio <= fecha_de_finalizacion)
);

alter table promocion
add column activo char(1) default "V";

CREATE TABLE promocion_dia(
    id_promocion_dia int not null auto_increment,
    primary key (id_promocion_dia)
);
alter table promocion_dia
add column id_promocion INT;

alter table promocion_dia
add column dias varchar(50);

alter table promocion_dia
add foreign key (id_promocion) references promocion(id_promocion);
ALTER TABLE promocion_dia ADD CONSTRAINT UQ_Promocion_Dia UNIQUE (id_promocion, dias);

INSERT INTO rol(nombre) values ("de canela");
INSERT INTO empleado(nombre,apellido_paterno,apellido_materno,celular,sueldo,id_rol,pass,administrator)
values ("Victor", "Escalante", "Alpuche", "1",30000,1,"a",1);
INSERT INTO pago(nombre) VALUES("Efectivo");

DROP TABLE IF EXISTS inventario;

CREATE TABLE inventario(
	id_producto INT NOT NULL AUTO_INCREMENT,
    entrada INT,
    salida INT,
    en_existencias INT,
    reponer BOOL,
    PRIMARY KEY(id_producto)
);