from conexion import Conexion 
class Padre_D:
	def insertar(INSERTAR,dato):
		with Conexion.ObtenerConexion() as conexion:
			cursor= conexion.cursor()
			cursor.execute(INSERTAR,dato)
			conexion.commit()
			print("el registro se guardo")
			conexion.close()	
	def modificar(MODIFICAR,dato):
		with Conexion.ObtenerConexion() as conexion:
			cursor= conexion.cursor()
			cursor.execute(MODIFICAR,dato)
			print("el registro se actualizo")	
	def eliminar(ELIMINAR,dato):
		with Conexion.ObtenerConexion() as conexion:
			cursor= conexion.cursor()
			cursor.execute(ELIMINAR,dato)
			print("el registro se ELIMINO")
	def consultar(SELECCIONAR):
		with Conexion.ObtenerConexion() as conexion:
			cursor= conexion.cursor()
			cursor.execute(SELECCIONAR)
			dato=cursor.fetchall()
		return dato	
	def consultardos(SELECCIONAR,datos):
		with Conexion.ObtenerConexion() as conexion:
			cursor= conexion.cursor()
			cursor.execute(SELECCIONAR,datos)
			dato=cursor.fetchall()
		return dato
"""
if __name__ == '__main__':
	from tkinter import *
	import sys
	import tkinter as tk
	from tkinter import *
	from tkinter import ttk
	v=Tk()
	SELECCIONARDOS='SELECT id_persona FROM persona ORDER BY id_persona'
	dato=Padre_D.consultar(SELECCIONARDOS)
	eidpersona=ttk.Combobox(v,width=13,font=("Roboto Cn",12))
	eidpersona.grid(row=0,column=1)
	eidpersona["value"]=dato
	v.mainloop()
"""