USE pollosexpress;
create table empleado (
	id_empleado int not null auto_increment,
    primary key (id_empleado)
);

alter table empleado
add column nombre nvarchar(100) not null;

alter table empleado
add column apellido_paterno nvarchar(100) not null;

alter table empleado
add column apellido_materno nvarchar(100) not null;

alter table empleado
add column celular varchar(11) not null;

alter table empleado
add column sueldo double not null;

alter table empleado
add column id_rol int;

alter table empleado
add column pass nvarchar(30);

alter table empleado
add column administrator bool not null;

alter table empleado
add foreign key (id_rol) references rol(id_rol);

alter table empleado
add constraint UQ_celular unique (celular);
