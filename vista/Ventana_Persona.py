import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import imutils
sys.path.append("../Controlador")
sys.path.append("../Modelo")
from conexion import Conexion
from Personas import Persona
from Hijos_D import Persona_D
class Ventana_Persona(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(background="white")
        self.title("Ventana Persona")
        self.geometry("610x300")
         
        #****************************************** Frame Label***********************************
        self.lframe_persona = LabelFrame(self,text="Datos Personales",font=("Roboto Cn",10),bg="white",fg="black")
        self.lframe_persona.place(x= 5, y=10, width= 600)
        #******************************************Frame Botones************************************
        self.lframe_boton = LabelFrame(self,text="Botones",font=("Roboto Cn",10),bg="white",fg="black")
        self.lframe_boton.place(x= 5, y=200, width= 600)
        #****************************************imagenes de los botones***************************************
        self.imguardar=Image.open("imagenes/guardar.png")
        self.imguardar = self.imguardar.resize((60, 60), Image.Resampling.LANCZOS)
        self.imguardar=ImageTk.PhotoImage(self.imguardar)
        
        self.imeditar=Image.open("imagenes/modificar.png")
        self.imeditar = self.imeditar.resize((60, 60), Image.Resampling.LANCZOS)
        self.imeditar=ImageTk.PhotoImage(self.imeditar)
        
        self.imeliminar=Image.open("imagenes/Eliminar.png")
        self.imeliminar = self.imeliminar.resize((60, 60), Image.Resampling.LANCZOS)
        self.imeliminar=ImageTk.PhotoImage(self.imeliminar)
        """
        self.imsalir=Image.open("imagenes/salir.png")
        self.imsalir = self.imsalir.resize((60, 60), Image.Resampling.LANCZOS)
        self.imsalir=ImageTk.PhotoImage(self.imsalir)

        self.imbuscar=Image.open("imagenes/buscar.png")
        self.imbuscar = self.imbuscar.resize((40, 40), Image.Resampling.LANCZOS)
        self.imbuscar=ImageTk.PhotoImage(self.imbuscar)
        """
        #***********************************label**********************************************
        self.lcedula=ttk.Label(self.lframe_persona,text="Cedula:",font=("Roboto Cn",12))
        self.lcedula.grid(row=0,column=0,pady=5,padx=5,sticky="w")
        self.lcedula.config(background="white")
        
        self.lpnombre=ttk.Label(self.lframe_persona,text="Primer Nombre:",font=("Roboto Cn",12))
        self.lpnombre.grid(row=1,column=0,pady=5,padx=5,sticky="w")
        self.lpnombre.config(background="white")

        self.lsnombre=ttk.Label(self.lframe_persona,text="Segundo Nombre:",font=("Roboto Cn",12))
        self.lsnombre.grid(row=1,column=2,pady=5,padx=5,sticky="w")
        self.lsnombre.config(background="white")
        
        self.lpapellido=ttk.Label(self.lframe_persona,text="Primer Apellido",font=("Roboto Cn",12))
        self.lpapellido.grid(row=2,column=0,pady=5,padx=5,sticky="w")
        self.lpapellido.config(background="white")

        self.lsapellido=ttk.Label(self.lframe_persona,text="Segundo Apellido",font=("Roboto Cn",12))
        self.lsapellido.grid(row=2,column=2,pady=5,padx=5,sticky="w")
        self.lsapellido.config(background="white")

        self.ltelefono=ttk.Label(self.lframe_persona,text="Telefono",font=("Roboto Cn",12))
        self.ltelefono.grid(row=3,column=0,pady=5,padx=5,sticky="w")
        self.ltelefono.config(background="white")

        self.lemail=ttk.Label(self.lframe_persona,text="Email",font=("Roboto Cn",12))
        self.lemail.grid(row=3,column=2,pady=5,padx=5,sticky="w")
        self.lemail.config(background="white")

        self.ltipo=ttk.Label(self.lframe_persona,text="Tipo",font=("Roboto Cn",12))
        self.ltipo.grid(row=4,column=0,pady=5,padx=5,sticky="w")
        self.ltipo.config(background="white")

        self.lestado=ttk.Label(self.lframe_persona,text="Estado",font=("Roboto Cn",12))
        self.lestado.grid(row=4,column=2,pady=5,padx=5,sticky="w")
        self.lestado.config(background="white")

        
#********************************Entradas**************************************
        self.ecedula=tk.Entry(self.lframe_persona,font=("Roboto Cn",12),width=17,bd=2)
        self.ecedula.grid(row=0,column=1)

        self.epnombre=tk.Entry(self.lframe_persona,font=("Roboto Cn",12),width=17,bd=2)
        self.epnombre.grid(row=1,column=1)

        self.esnombre=tk.Entry(self.lframe_persona,font=("Roboto Cn",12),width=17,bd=2)
        self.esnombre.grid(row=1,column=3)

        self.epapellido=tk.Entry(self.lframe_persona,font=("Roboto Cn",12),width=17,bd=2)
        self.epapellido.grid(row=2,column=1)

        self.esapellido=tk.Entry(self.lframe_persona,font=("Roboto Cn",12),width=17,bd=2)
        self.esapellido.grid(row=2,column=3)

        self.etelefono=tk.Entry(self.lframe_persona,font=("Roboto Cn",12),width=17,bd=2)
        self.etelefono.grid(row=3,column=1)

        self.eemail=tk.Entry(self.lframe_persona,font=("Roboto Cn",12),width=17,bd=2)
        self.eemail.grid(row=3,column=3)

        self.etipo=ttk.Combobox(self.lframe_persona,font=("Roboto Cn",12),width=15)
        self.etipo.grid(row=4,column=1)
        self.etipo["value"]=["Propietario","Visitante"]

        self.eestado=ttk.Combobox(self.lframe_persona,font=("Roboto Cn",12),width=15)
        self.eestado.grid(row=4,column=3)
        self.eestado["value"]=["Activo","inactivo"]
#*********************************botones**************************************
        self.bguardar=ttk.Button(self.lframe_boton,image=self.imguardar,text="Guardar",command=self.guardarpersona)
        self.bguardar.grid(row=5,column=0,pady=10,padx=30)
        self.bmodificar=ttk.Button(self.lframe_boton,image=self.imeditar,text="Modificar")
        self.bmodificar.grid(row=5,column=1,pady=10,padx=30)
        self.beliminar=ttk.Button(self.lframe_boton,image=self.imeliminar,text="Eliminar")
        self.beliminar.grid(row=5,column=2,pady=10,padx=30)
        self.bsalir=ttk.Button(self.lframe_boton,text="Salir",command=self.destroy)
        self.bsalir.grid(row=5,column=3,pady=10,padx=20)
        self.focus()
        self.grab_set() 
     
    def guardarpersona(self):
        a=set(self.ecedula.get())
        if (len(a)==0):
            messagebox.showinfo(message="¿Digite la cedula  porfavor?", title="validar cedula")
            self.ecedula.focus_set()
        else:
            m=messagebox.askquestion(message="¿Desea Guardar el registro?", title="Guardar")
            if m=="yes":
                perso=Persona(self.ecedula.get(),self.epnombre.get(),self.esnombre.get(),self.epapellido.get(),self.esapellido.get(),self.etelefono.get(),self.eemail.get(),self.etipo.get(),self.eestado.get())
                INSERTAR='INSERT INTO persona VALUES(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                dato=[perso.cedula,perso.pnombre,perso.snombre,perso.papellido,perso.sapellido,perso.telefono,perso.email,perso.estado,perso.tipo]
                Persona_D.insertar(INSERTAR,dato)
                messagebox.showinfo(message="¿Se guardo correctamente el registro?", title="Guardar persona")
            else:
                messagebox.showinfo(message="¿El registro no se guardo?", title="Guardar persona")