from tkinter import *
import tkinter as tk
from Ventana_Persona import Ventana_Persona
from Ventana_Automovil import Ventana_Automovil
from Ventana_Marca import Ventana_Marca
from Ventana_Modelo import Ventana_Modelo
from Ventana_Color import Ventana_Color
from tkinter import ttk
class Ventana_Principal(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1100, height=600)
        self.title("Vision Artificial")
        menuframe=Frame(self,bg="black")
        menuframe.place(x= 0, y=0, width= 1100)
        persona=Menubutton(menuframe,
                              text="Persona",
                              bg="white",
                              activeforeground='black',
                              activebackground='gray52')
        automovil=Menubutton(menuframe,
                              text="Automovil",
                              bg="white",
                              activeforeground='black',
                              activebackground='gray52')
        historial=Menubutton(menuframe,
                              text="Historial",
                              bg="white",
                              activeforeground='black',
                              activebackground='gray52')
        apartamento=Menubutton(menuframe,
                              text="Apartamento",
                              bg="white",
                              activeforeground='black',
                              activebackground='gray52')
        camaras=Menubutton(menuframe,
                              text="Camaras",
                              bg="white",
                              activeforeground='black',
                              activebackground='gray52')
        parqueadero=Menubutton(menuframe,
                              text="Parqueadero",
                              bg="white",
                              activeforeground='black',
                              activebackground='gray52')
        salir=Menubutton(menuframe,
                              text="Salir",
                              bg="white",
                              activeforeground='black',
                              activebackground='gray52')
        menu_persona=Menu(persona,tearoff=0)
        menu_persona.add_command(label="Registro",
                                 command=Ventana_Persona,
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_automovil=Menu(automovil,tearoff=0)
        menu_automovil.add_command(label="Registro",
                                 command=Ventana_Automovil,
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_automovil.add_command(label="Marca",
                                 command=Ventana_Marca,
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_automovil.add_command(label="Modelo",
                                 command=Ventana_Modelo,
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_automovil.add_command(label="Color",
                                 command=Ventana_Color,
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_historial=Menu(historial,tearoff=0)
        menu_historial.add_command(label="Historial",
                                 command=lambda:print("hola"),
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_apartamento=Menu(apartamento,tearoff=0)
        menu_apartamento.add_command(label="Apartamento",
                                 command=lambda:print("hola"),
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_camaras=Menu(camaras,tearoff=0)
        menu_camaras.add_command(label="Camaras",
                                 command=lambda:print("hola"),
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_parqueadero=Menu(parqueadero,tearoff=0)
        menu_parqueadero.add_command(label="Parqueadero",
                                 command=lambda:print("hola"),
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_parqueadero.add_command(label="Celda",
                                 command=lambda:print("hola"),
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_salir=Menu(salir,tearoff=0)
        menu_salir.add_command(label="Salir",
                                 command=lambda:self.destroy(),
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        persona.config(menu=menu_persona)
        persona.pack(side="left")
        automovil.config(menu=menu_automovil)
        automovil.pack(side="left")
        historial.config(menu=menu_historial)
        historial.pack(side="left")
        apartamento.config(menu=menu_apartamento)
        apartamento.pack(side="left")
        camaras.config(menu=menu_camaras)
        camaras.pack(side="left")
        parqueadero.config(menu=menu_parqueadero)
        parqueadero.pack(side="left")
        salir.config(menu=menu_salir)
        salir.pack(side="left")
        
        
        #from Ventana_color import Ventana_Color
        #from Ventana_Persona import Ventana_Persona
        #from Ventana_marca import Ventana_Marca
        #from Ventana_modelo import Ventana_Modelo
        #from Ventana_automovil import Ventana_Automovil
        #from Ventana_celda import Ventana_Celda
        #from Ventana_parqueadero import Ventana_Parqueadero
        