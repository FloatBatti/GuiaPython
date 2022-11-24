/*
create database frutas_magicas;
use frutas_magicas;
*/

create table if not exists provincias(
id_provincia bigint auto_increment,
nombre_provincia varchar(50) not null,

constraint pk_provincia primary key(id_provincia),
constraint unq_nombre_provincia unique(nombre_provincia)
);

create table if not exists ciudades(
id_ciudad bigint auto_increment,
nombre_ciudad varchar (50) not null,
id_provincia bigint not null,

constraint pk_ciudad primary key(id_ciudad),
constraint unq_nombre_ciudad_provincia unique(nombre_ciudad, id_provincia),
constraint fk_ciudad_provincia foreign key(id_provincia) references provincias(id_provincia)
);

create table if not exists locales(
id_local bigint auto_increment,
nombre_local varchar(50) not null, 
direccion_local varchar(50) not null,
telefono_local varchar(50) not null,
id_ciudad bigint not null,

constraint pk_local primary key(id_local),
constraint unq_nombre_local unique (nombre_local),
constraint fk_local_ciudad foreign key(id_ciudad) references ciudades(id_ciudad)
);

create table if not exists proveedores(
id_proveedor bigint auto_increment,
nombre_proveedor varchar(50) not null, 
telefono_proveerdor varchar(20) not null,
correo_proveedor varchar(50) not null,
cbu varchar(50) not null,

constraint pk_proveedor primary key(id_proveedor),
constraint unq_correo_proveedor unique(correo_proveedor),
constraint unq_cbu unique(cbu)
);

create table if not exists categoria(
id_categoria bigint auto_increment,
nombre_categoria varchar(50) not null, 

constraint pk_categoria primary key(id_categoria),
constraint unq_nombre_categoria unique(nombre_categoria)
);

create table if not exists cargos(
id_cargo bigint auto_increment,
nombre_cargo varchar(50) not null,

constraint pk_cargo primary key(id_cargo),
constraint unq_nombre_cargo unique(nombre_cargo)
);

create table if not exists empleados(
id_empleado bigint auto_increment,
nombre_empleado varchar(50) not null, 
dni varchar(8) not null,
telefono varchar(20) not null,
cbu varchar(50) not null,
id_cargo bigint not null,
id_local bigint not null,

constraint pk_empleado primary key(id_empleado),
constraint unq_dni unique(dni),
constraint unq_cbu unique(cbu),
constraint fk_empleado_cargo foreign key(id_cargo) references cargos(id_cargo),
constraint fk_empleado_local foreign key(id_local) references locales (id_local)
);


create table if not exists productos(
id_producto bigint auto_increment,
nombre_producto varchar(50) not null,
id_categoria bigint not null,

constraint pk_producto primary key(id_producto),
constraint unq_nombre_producto unique(nombre_producto),
constraint fk_producto_categoria foreign key(id_categoria) references categoria (id_categoria)
);

create table if not exists stock(
id_stock bigint auto_increment,
cantidad int not null,
id_producto bigint not null,
id_local bigint not null,

constraint pk_stock primary key(id_stock),
constraint fk_stock_producto foreign key(id_producto) references productos(id_producto),
constraint fk_stock_local foreign key(id_local) references locales(id_local),
constraint chk_cantidad_stock check (cantidad>=0)
);

create table if not exists pedidos(
id_pedido bigint auto_increment,
cantidad varchar (50) not null,
id_proveedor bigint not null,
id_producto bigint not null,

constraint pk_pedido primary key(id_pedido),
constraint fk_pedido_proveedor foreign key(id_proveedor) references proveedores (id_proveedor),
constraint fk_pedido_producto foreign key(id_producto) references productos(id_producto),
constraint chk_cantidad_pedido check (cantidad >= 0)
);



