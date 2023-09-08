from tkinter import *
import tkinter as tk
from tkinter import ttk
class Ventana_Principal(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("Vision Artificial")
        barra = tk.Menu(historial)
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
        barra.add_cascade(menu=Automovil, label="Apartamento")
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
if __name__ == '__main__':
    
    Ventana_Principal=Ventana_Principal()
    Ventana_Principal.mainloop()
