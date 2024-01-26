USE pollosexpress;
create table produto (
	id_producto int not null auto_increment,
    primary key (id_producto)
);

alter table producto
add column nombre nvarchar(100) not null;

alter table producto
add column descripcion nvarchar(255) not null;

alter table producto
add column precio double not null;

alter table producto
add column imagen text not null;