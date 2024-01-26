USE pollosexpress;
create table venta_producto (
	id_venta_producto int not null auto_increment,
    primary key (id_venta_producto)
);

alter table venta_producto
add column cantidad int not null;

alter table venta_producto
add column id_venta int;

alter table venta_producto
add column id_producto int;

alter table venta_producto
add foreign key (id_venta) references venta(id_venta);

alter table venta_producto
add foreign key (id_producto) references producto(id_producto);