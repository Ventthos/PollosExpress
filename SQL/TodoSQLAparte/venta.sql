USE pollosexpress;
create table venta(
	id_venta int not null auto_increment,
    primary key (id_venta)
);

alter table venta
add column fecha_De_Venta date not null;

alter table venta
add column total_De_Compra double not null;

alter table venta
add column id_pago int;

alter table venta
add column id_empleado int;

alter table venta
add column id_cliente int;

alter table venta
add foreign key (id_pago) references pago(id_pago);

alter table venta
add foreign key (id_empleado) references empleado(id_empleado);

alter table venta
add foreign key (id_cliente) references cliente(id_cliente);