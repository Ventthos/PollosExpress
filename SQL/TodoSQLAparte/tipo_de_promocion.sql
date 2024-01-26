USE pollosexpress;
create table tipo_de_promocion(
	id_tipo_promocion int not null auto_increment,
    primary key (id_tipo_promocion)
);

alter table tipo_de_promocion
add column nombre nvarchar(100) not null;
 
alter table tipo_de_promocion
add column codigo nvarchar(50) not null;