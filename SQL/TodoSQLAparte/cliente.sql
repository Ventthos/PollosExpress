USE pollosexpress;
create table cliente(
	id_cliente int not null auto_increment
);

alter table cliente
add column nombre nvarchar(50) not null;

alter table cliente
add column apellido_paterno nvarchar(50) not null;

alter table cliente
add column apellido_materno nvarchar(50) not null;

alter table cliente
add column celular varchar(11) not null;

alter table cliente 
add column direccion nvarchar(255) not null;