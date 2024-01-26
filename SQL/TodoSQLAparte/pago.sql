USE pollosexpress;
create table pago(
	id_pago int not null auto_increment,
    primary key (id_pago)
);

alter table pago
add column nombre nvarchar(50) not null;