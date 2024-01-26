USE pollosexpress;
create table rol(
    id_rol int not null auto_increment,
    primary key (id_rol)
);

alter table rol
add column nombre nvarchar(50) not null;

alter table rol
add constraint UQ_nombre unique (nombre)