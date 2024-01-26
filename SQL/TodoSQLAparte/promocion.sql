USE pollosexpress;
create table promocion(
	id_promocion int not null auto_increment,
    primary key (id_promocion)
);
alter table promocion
add column descripcion nvarchar(200);

alter table promocion
add column fecha_de_inicio date not null;

alter table promocion
add column fecha_de_finalizacion date;

alter table promocion
add column id_producto int;

alter table promocion
add column id_tipo_promocion int;

alter table promocion
add foreign key (id_producto) references producto(id_producto);

alter table promocion
add foreign key (id_tipo_promocion) references tipo_de_promocion(id_tipo_promocion);

alter table promocion
add constraint fecha_valida check (fecha_de_inicio <= fecha_de_finalizacion)