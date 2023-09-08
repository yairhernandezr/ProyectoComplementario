import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import imutils
from tkinter import messagebox
sys.path.append("../Controlador")
sys.path.append("../Modelo")
from conexion import Conexion
from Color import Color
from Hijos_D import Color_D
class Ventana_Color(tk.Toplevel):
    """Clase Ventana_Color """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #****************************************Configuracion Ventana **************************
        self.config(background="black")
        self.title("Ventana Color")
        self.geometry("365x200")
         
        #****************************************** Frame Label***********************************
        self.lframe_color = LabelFrame(self,text="Color",font=("Roboto Cn",10),bg="black",fg="white")
        self.lframe_color.place(x= 5, y=10, width= 350)
        #******************************************Frame Botones************************************
        self.lframe_boton = LabelFrame(self,text="Botones",font=("Roboto Cn",10),bg="black",fg="white")
        self.lframe_boton.place(x= 5, y=80, width= 350)
        #****************************************label *******************************************
        self.lcolor=Label(self.lframe_color,text="Nombre del Color",font=("Roboto Cn",12),bg="black",fg="white")
        self.lcolor.grid(row=0,column=0,padx=10,pady=10)
        #*****************************************Entrada *****************************************
        self.ecolor=Entry(self.lframe_color,font=("Roboto Cn",12),bg="black",fg="white",bd=2)
        self.ecolor.grid(row=0,column=1)
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
        self.bguarda=Button(self.lframe_boton,image=self.imguardar,bg="black",bd="0")
        self.bguarda.grid(row=5,column=0,pady=10,padx=10)
        self.bmodificar=Button(self.lframe_boton,image=self.imeditar,bg="black",bd="0")
        self.bmodificar.grid(row=5,column=1,pady=10,padx=10)
        self.beliminar=Button(self.lframe_boton,image=self.imeliminar,bg="black",bd="0")
        self.beliminar.grid(row=5,column=2,pady=10,padx=10)
        self.bsalir=Button(self.lframe_boton,image=self.imsalir,bg="black",bd="0",command=self.destroy)
        self.bsalir.grid(row=5,column=3,pady=10,padx=10)
        self.focus()
        self.grab_set()
        #************************************ Metodo Guaradar *******************************************    
    def guardarcolor(self):
        if self.ecolor.get()==" ":
            messagebox.showinfo(message="¿Digite el nombre del color porfavor?", title="validar color")
            self.ecolor.focus_set()
        else:
            m=messagebox.askquestion(message="¿Desea Guardar el registro?", title="Guardar")
            if m=="yes":
                color=Color(self.ecolor.get(),)
                INSERTAR='INSERT INTO color VALUES(null,%s)'
                dato=[color.color]
                Color_D.insertar(INSERTAR,dato)
                messagebox.showinfo(message="¿Se guardo correctamente el registro?", title="Guardar color")
            else:
                messagebox.showinfo(message="¿El registro no se guardo?", title="Guardar color")
        