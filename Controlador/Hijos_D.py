import sys 
sys.path.append("../Modelo")
from Personas import Persona
from Automovil import Automovil
from Modelos    import Modelos
from Marca import Marca 
from Color import Color 
from Celda import Celda 
from Parqueadero import Parqueadero 
from Apartamento import Apartamento
from Historial import Historial 
from Padre import Padre_D
import pandas as pd
class Persona_D(Padre_D):
	pass
class Apartamento_D(Padre_D):
	pass 
class Automovil_D(Padre_D):
	pass
class Camaras_D(Padre_D):
	pass
class Parqueadero_D(Padre_D):
	pass
class Historial_D(Padre_D):
	pass
class Modelo_D(Padre_D):
	pass
class Marca_D(Padre_D):
	pass
class Color_D(Padre_D):
	pass
class Celda_D(Padre_D):
	pass
"""	
if __name__ == '__main__':
	
	
	# ****************INSERTAR PERSONA**************
	INSERTAR='INSERT INTO persona VALUES(null,%s,%s,%s,%s,%s)'
	persona1=Persona("maria",777777,"maria@gmail.com",1,"Propietario")
	dato=[persona1.nombre,persona1.telefono,persona1.email,persona1.estado,persona1.tipo]
	Persona_D.insertar(INSERTAR,dato)
	#****************MOSTRAR PERSONA***************
	#**********************************************
	SELECCIONAR='SELECT * FROM persona'
	datoz=Persona_D.consultar(SELECCIONAR)
	df=pd.DataFrame(datoz,columns=["ID","Nombre","Telefono","Email","Estado","Tipo"])
	print(df)

	#***********************************************
	# *******AUTOMOVIL INSERTAR***************
	#auto=Automovil("BBB124",1,2,23,1,105)
	#INSERTAR='INSERT INTO auto VALUES(null,%s,%s,%s,%s,%s,%s)'
	#dato=[auto.placa,auto.id_marca,auto.id_modelo,auto.id_color,auto.estado,auto.id_persona]
	#Automovil_D.insertar(INSERTAR,dato)
	#*********AUTOMOVIL MOSTRAR**************
	#SELECCIONAR='SELECT * FROM auto'
	#datoz=Automovil_D.consultar(SELECCIONAR)
	#df=pd.DataFrame(datoz,columns=["id_automovil","Placa","Marca","Modelo","Color","Estado","id_persona"])
	#print()


	#***********APARTAMENTO INSERTAR***********
	#******************************************

	apartamento=Apartamento(5,201,2)
	INSERTAR='INSERT INTO apartamento VALUES(null,%s,%s,%s)'
	dato=[apartamento.bloque,apartamento.numero,apartamento.id_persona]
	Apartamento_D.insertar(INSERTAR,dato)
	SELECCIONAR='SELECT * FROM apartamento'
	#***********APARTAMENTO MOSTRAR*********
	#***************************************
	datoz=Apartamento_D.consultar(SELECCIONAR)
	df=pd.DataFrame(datoz,columns=["ID","Bloque","Numero","Id_persona"])
	print(df)
	#***************************************
	#***************************************

	colo=Color("Blanco")
	INSERTAR='INSERT INTO color VALUES(null,%s)'
	dato=[colo.color]
	Color_D.insertar(INSERTAR,dato)
	#*********AUTOMOVIL MOSTRAR**************
	SELECCIONAR='SELECT * FROM color'
	datoz=Automovil_D.consultar(SELECCIONAR)
	df=pd.DataFrame(datoz,columns=["id_color","Color"])
	print(df)
	
	colo=Color("Verde")
	INSERTAR='INSERT INTO color VALUES(null,%s)'
	dato=[colo.color]
	Color_D.insertar(INSERTAR,dato)
	#*********AUTOMOVIL MOSTRAR**************
	SELECCIONAR='SELECT * FROM color'
	datoz=Automovil_D.consultar(SELECCIONAR)
	df=pd.DataFrame(datoz,columns=["id_color","Color"])
	print(df)
"""