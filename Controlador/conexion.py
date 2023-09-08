import mysql.connector
class Conexion:
	def ObtenerConexion():
	    conexion = mysql.connector.connect(user='root',
	                                password='',
	                                host='localhost',
	                                database='parquin')
	    return conexion
