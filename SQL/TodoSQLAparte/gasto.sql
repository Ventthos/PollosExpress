USE pollosexpress;
create table gasto (
	id_gasto int not null auto_increment,
    primary key (id_gasto)
);

alter table gasto
add column descripcion varchar(150) not null;

alter table gasto
add column monto double not null;

alter table gasto
add column fecha date not null;

alter table gasto
add column id_empleado int;

alter table gasto
add foreign key (id_empleado) references empleado(id_empleado);