from tkinter import *
import tkinter as tk
from Ventana_Persona import Ventana_Persona
from tkinter import ttk
class Ventana_Principal(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("Vision Artificial")
        menuframe=Frame(self,bg="black")
        menuframe.pack(side="top",fill='x')
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
        menu_persona.add_command(label="silvia",
                                 command=Ventana_Persona,
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_automovil=Menu(automovil,tearoff=0)
        menu_automovil.add_command(label="Registro",
                                 command=lambda:print("hola"),
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_automovil.add_command(label="Marca",
                                 command=lambda:print("Mercedes"),
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_automovil.add_command(label="Modelo",
                                 command=lambda:print("2023"),
                                 background="black",
                                 foreground="white",
                                 activeforeground="black",
                                 activebackground="gray52")
        menu_automovil.add_command(label="Color",
                                 command=lambda:print("Rojo"),
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
        menu_salir=Menu(salir,tearoff=0)
        menu_salir.add_command(label="Salir",
                                 command=self.destroy,
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
        salir.config(menu=menu_salir)
        salir.pack(side="left")
        """
        barra = tk.Menu()
        #****************************Historial****************************************
        historial = tk.Menu(barra, tearoff=False)
        historial.add_cascade(label="historia")
        barra.add_cascade(menu=historial, label="Historia")
        #*********************************Automovil************************************
        persona = tk.Menu(barra, tearoff=False)
        persona.add_cascade(label="Persona")
        barra.add_cascade(menu=persona, label="Persona")
        #*********************************persona************************************
        Automovil = tk.Menu(barra, tearoff=False)
        Automovil.add_cascade(label="Automovil")
        Automovil.add_cascade(label="Marca")
        Automovil.add_cascade(label="Modelo")
        Automovil.add_cascade(label="Color")
        barra.add_cascade(menu=Automovil, label="Automovil")
        #**************************************apartamento*********************************
        Apartamento = tk.Menu(barra, tearoff=False)
        Apartamento.add_cascade(label="Apartamento")
        barra.add_cascade(menu=Apartamento, label="Apartamento")
         #*************************************camaras**********************************
        Camaras = tk.Menu(barra, tearoff=False)
        Camaras.add_cascade(label="Camaras")
        barra.add_cascade(menu=Camaras, label="Camaras")
        self.config(menu=barra)
         #*************************************Parqueaderos**********************************
        Parqueaderos = tk.Menu(barra, tearoff=False)
        Parqueaderos.add_cascade(label="Parqueaderos")
        barra.add_cascade(menu=Parqueaderos, label="Parqueaderos")
        self.config(menu=barra)
        
        #from Ventana_color import Ventana_Color
        #from Ventana_Persona import Ventana_Persona
        #from Ventana_marca import Ventana_Marca
        #from Ventana_modelo import Ventana_Modelo
        #from Ventana_automovil import Ventana_Automovil
        #from Ventana_celda import Ventana_Celda
        #from Ventana_parqueadero import Ventana_Parqueadero
        """