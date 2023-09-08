import sqlite3
import pandas as pd 
conexion=sqlite3.connect("proyecto.db")
def insertauto(conexion):
	placa=input("¿Digite la placa:")
	marca=input("¿Digite la marca:")
	modelo=input("¿Digite el modelo:")
	color=input("¿Digite el color:")
	dato=(placa,marca,modelo,color)
	cursor=conexion.cursor()
	cursor.execute("INSERT INTO automovil values(?,?,?,?)",dato)
	conexion.commit()
	print("su registro se guardo en la base")
#for i in range(5):	
	insertauto(conexion)

def modificar(conexion):
	cursor=conexion.cursor()
	cursor.execute("UPDATE automovil SET marca='lelo', modelo='2023', color='pink' where placa='AAQ-784' " )
	conexion.commit()
#modificar(conexion)
def crearnuevatabla(conexion):
	df = pd.read_sql_query("SELECT * from automovil", conexion)
	df = df[df.marca == "Mercedes"]
	df.to_sql("df", conexion, if_exists="replace")
	print("se creo la nueva tbla")
crearnuevatabla(conexion)
def mostrar(conexion):
	df = pd.read_sql_query("SELECT * from automovil", conexion)
	print(df)
	
#mostrar(conexion)

def cerrarbase(conexion):
	conexion.close()
cerrarbase(conexion)
"""
def mostrar(conexion):
	cursor=conexion.cursor()
	for row in cursor.execute('SELECT * FROM automovil'):
		print(row)
mostrar(conexion)

def mostrar(conexion):
	cursor=conexion.cursor()
	cursor.execute("SELECT * FROM automovil")
	dato=cursor.fetchall()
	return dato 
dato=mostrar(conexion)
df=pd.DataFrame(dato)
print(df)
"""
