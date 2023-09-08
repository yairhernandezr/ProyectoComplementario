import sqlite3
import pandas as pd 
conexion=sqlite3.connect("proyecto.db")

def creartabla(conexion):
	cursor=conexion.cursor()
	sql="""
	DROP TABLE IF EXISTS persona;
	DROP TABLE IF EXISTS automovil;
	DROP TABLE IF EXISTS marca;
	DROP TABLE IF EXISTS modelo;
	DROP TABLE IF EXISTS color;
	DROP TABLE IF EXISTS apartamento;	
	DROP TABLE IF EXISTS visitante;
	DROP TABLE IF EXISTS arrendatario;
	DROP TABLE IF EXISTS propietario;

	CREATE TABLE persona(
	id_persona INTEGER PRIMARY KEY AUTOINCREMENT,
	cedula VARCHAR(20),
	pnombre VARCHAR(20),
	snombre VARCHAR(20),
	papellido VARCHAR(20),
	sapellido VARCHAR(20),
	telefono VARCHAR(20),
	email VARCHAR(20),
	tipo VARCHAR(20));

	CREATE TABLE propietario(
	celula VARCHAR(20) PRIMARY KEY ,
	id_propietario INTEGER,
	estado VARCHAR(20),
	FOREIGN KEY (id_propietario) REFERENCES persona(id_persona));

	CREATE TABLE arrendatario(
	cedula VARCHAR(20) PRIMARY KEY ,
	id_persona INTEGER,
	celula VARCHAR(20),
	estado VARCHAR(20),
	FOREIGN KEY (id_persona) REFERENCES persona(id_persona),
	FOREIGN KEY (celula) REFERENCES propietario(celula));

	CREATE TABLE visitante(
	cedula VARCHAR(20) PRIMARY KEY ,
	id_persona INTEGER,
	id_apartamento INTEGER,
	estado VARCHAR(20),
	FOREIGN KEY (id_persona) REFERENCES persona(id_persona),
	FOREIGN KEY (id_apartamento) REFERENCES apartamento(id_apartamento));

	CREATE TABLE apartamento(
	id_apartamento INTEGER PRIMARY KEY AUTOINCREMENT,
	numero VARCHAR(20),
	bloque VARCHAR(5),
	id_persona INTEGER,
	FOREIGN KEY (id_persona) REFERENCES persona(id_persona));

	CREATE TABLE automovil(
	id_automovil INTEGER PRIMARY KEY AUTOINCREMENT,
	id_persona INTEGER,
	id_marca  INTEGER not null,
	id_modelo INTEGER not null,
	id_color INTEGER not null,
	placa VARCHAR(20),
	estado VARCHAR(30),
	FOREIGN KEY (id_persona) REFERENCES persona(id_persona),
	FOREIGN KEY (id_marca) REFERENCES marca(id_marca),
	FOREIGN KEY (id_modelo) REFERENCES modelo(id_modelo),
	FOREIGN KEY (id_color) REFERENCES color(id_color));

	CREATE TABLE marca(
	id_marca INTEGER PRIMARY KEY AUTOINCREMENT,
	marca VARCHAR(20));

	CREATE TABLE modelo(
	id_modelo INTEGER PRIMARY KEY AUTOINCREMENT,
	modelo VARCHAR(20));

	CREATE TABLE color(
	id_color INTEGER PRIMARY KEY AUTOINCREMENT,
	color VARCHAR(20));
	"""
	cursor.executescript(sql)
	print("la base de datos esta creada")
creartabla(conexion)
