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
from Marca import Marca
from Hijos_D import Marca_D
class Ventana_Marca(tk.Toplevel):
    """Clase Ventana_Marca """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #****************************************Configuracion Ventana **************************
        self.config(background="black")
        self.title("Ventana Marca")
        self.geometry("365x200")
         
        #****************************************** Frame Label***********************************
        self.lframe_marca = LabelFrame(self,text="Marca",font=("Roboto Cn",10),bg="black",fg="white")
        self.lframe_marca.place(x= 5, y=10, width= 350)
        #******************************************Frame Botones************************************
        self.lframe_boton = LabelFrame(self,text="Botones",font=("Roboto Cn",10),bg="black",fg="white")
        self.lframe_boton.place(x= 5, y=80, width= 350)
        #****************************************label *******************************************
        self.lmarca=Label(self.lframe_marca,text="Nombre Marca",font=("Roboto Cn",12),bg="black",fg="white")
        self.lmarca.grid(row=0,column=0,padx=10,pady=10)
        #*****************************************Entrada *****************************************
        self.emarca=Entry(self.lframe_marca,font=("Roboto Cn",12),bg="black",fg="white",bd=2)
        self.emarca.grid(row=0,column=1)
        #****************************************** Imagenes  de los Botones ******************************
        self.imguardar=Image.open("imagenes/guardar.png")
        self.imguardar = self.imguardar.resize((60, 60), Image.Resampling.LANCZOS)
        self.imguardar=ImageTk.PhotoImage(self.imguardar)

        self.imeditar=Image.open("imagenes/editar.png")
        self.imeditar = self.imeditar.resize((60, 60), Image.Resampling.LANCZOS)
        self.imeditar=ImageTk.PhotoImage(self.imeditar)

        self.imeliminar=Image.open("imagenes/eliminar.png")
        self.imeliminar = self.imeliminar.resize((60, 60), Image.Resampling.LANCZOS)
        self.imeliminar=ImageTk.PhotoImage(self.imeliminar)

        self.imsalir=Image.open("imagenes/salir.png")
        self.imsalir = self.imsalir.resize((60, 60), Image.Resampling.LANCZOS)
        self.imsalir=ImageTk.PhotoImage(self.imsalir)

        self.imbuscar=Image.open("imagenes/buscar.png")
        self.imbuscar = self.imbuscar.resize((40, 40), Image.Resampling.LANCZOS)
        self.imbuscar=ImageTk.PhotoImage(self.imbuscar)
        #**************************************** Botones ****************************************
        self.bguardar=Button(self.lframe_boton,image=self.imguardar,bg="black",bd="0",command=self.guardarmarca)
        self.bguardar.grid(row=5,column=0,pady=10,padx=10)
        self.bmodificar=Button(self.lframe_boton,image=self.imeditar,bg="black",bd="0")
        self.bmodificar.grid(row=5,column=1,pady=10,padx=10)
        self.beliminar=Button(self.lframe_boton,image=self.imeliminar,bg="black",bd="0")
        self.beliminar.grid(row=5,column=2,pady=10,padx=10)
        self.bsalir=Button(self.lframe_boton,image=self.imsalir,bg="black",bd="0",command=self.destroy)
        self.bsalir.grid(row=5,column=3,pady=10,padx=10)
        self.focus()
        self.grab_set()
        #************************************ Metodo Guaradar *******************************************    
    def guardarmarca(self):
        if self.emarca.get()==" ":
            messagebox.showinfo(message="¿Digite el nombre de la Marca porfavor?", title="validar Marca")
            self.emarca.focus_set()
        else:
            m=messagebox.askquestion(message="¿Desea Guardar el registro?", title="Guardar")
            if m=="yes":
                marca=Marca(self.emarca.get(),)
                INSERTAR='INSERT INTO marca VALUES(null,%s)'
                dato=[marca.marca]
                Marca_D.insertar(INSERTAR,dato)
                messagebox.showinfo(message="¿Se guardo correctamente el registro?", title="Guardar Marca")
            else:
                messagebox.showinfo(message="¿El registro no se guardo?", title="Guardar color")
        

