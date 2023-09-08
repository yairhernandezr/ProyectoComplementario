
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
sys.path.append("../Controlador")
sys.path.append("../Modelo")
from conexion import Conexion
from Personas import Persona
from Hijos_D import Persona_D
class Ventana_Persona(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x200")
        self.title("Ventana secundaria")

#********************************Label" Frame**************************************
        
#********************************Label**************************************
        self.lcedula=ttk.Label(self,text="Cedula",font=("Roboto Cn",12))
        self.lcedula.grid(row=0,column=0,pady=5,padx=5,sticky="w")
        self.lcedula.config(background="white")
        self.lpnombre=ttk.Label(self,text="Primer nombre",font=("Roboto Cn",12))
        self.lpnombre.grid(row=1,column=0,pady=5,padx=5,sticky="w")
        self.lpnombre.config(background="white")
        self.lpapellido=ttk.Label(self,text="Primer apellido",font=("Roboto Cn",12))
        self.lpapellido.grid(row=2,column=0,pady=5,padx=5,sticky="w")
        self.lpapellido.config(background="white")
        self.ltelefono=ttk.Label(self,text="Telefono",font=("Roboto Cn",12))
        self.ltelefono.grid(row=3,column=0,pady=5,padx=5,sticky="w")
        self.ltelefono.config(background="white")
        self.ltipo=ttk.Label(self,text="Tipo",font=("Roboto Cn",12))
        self.ltipo.grid(row=4,column=0,pady=5,padx=5,sticky="w")
        self.ltipo.config(background="white")       

        self.lsnombre=ttk.Label(self,text="Segundo nombre",font=("Roboto Cn",12))
        self.lsnombre.grid(row=1,column=2,pady=5,padx=5,sticky="w")
        self.lsnombre.config(background="white")
        self.lsapellido=ttk.Label(self,text="Segundo apellido",font=("Roboto Cn",12))
        self.lsapellido.grid(row=2,column=2,pady=5,padx=5,sticky="w")
        self.lsapellido.config(background="white")
        self.lemail=ttk.Label(self,text="Telefono",font=("Roboto Cn",12))
        self.lemail.grid(row=3,column=2,pady=5,padx=5,sticky="w")
        self.lemail.config(background="white")
#********************************Entradas**************************************
        self.ecedula=tk.Entry(self,font=("Roboto Cn",12),width=17,bd=2)
        self.ecedula.grid(row=0,column=1)
        self.epnombre=tk.Entry(self,font=("Roboto Cn",12),width=17,bd=2)
        self.epnombre.grid(row=1,column=1)
        self.epapellido=tk.Entry(self,font=("Roboto Cn",12),width=17,bd=2)
        self.epapellido.grid(row=2,column=1)
        self.etelefono=tk.Entry(self,font=("Roboto Cn",12),width=17,bd=2)
        self.etelefono.grid(row=3,column=1)        
        self.etipo=ttk.Combobox(self,font=("Roboto Cn",12),width=15)
        self.etipo.grid(row=4,column=1)
        self.etipo["value"]=["Propietario","Visitante"]

        self.esnombre=tk.Entry(self,font=("Roboto Cn",12),width=17,bd=2)
        self.esnombre.grid(row=1,column=3)
        self.esapellido=tk.Entry(self,font=("Roboto Cn",12),width=17,bd=2)
        self.esapellido.grid(row=2,column=3)
        self.eemail=tk.Entry(self,font=("Roboto Cn",12),width=17,bd=2)
        self.eemail.grid(row=3,column=3)
#*********************************botones**************************************
        self.bguardar=ttk.Button(self,text="Guardar",command=self.guardarpersona)
        self.bguardar.grid(row=5,column=0,pady=10,padx=30)
        self.bmodificar=ttk.Button(self,text="Modificar")
        self.bmodificar.grid(row=5,column=1,pady=10,padx=30)
        self.beliminar=ttk.Button(self,text="Eliminar")
        self.beliminar.grid(row=5,column=2,pady=10,padx=30)
        self.bsalir=ttk.Button(self,text="Salir")
        self.bsalir.grid(row=5,column=3,pady=10,padx=20)
        self.focus()
        self.grab_set()    
    def guardarpersona(self):
        if self.enombre.get()==" ":
            messagebox.showinfo(message="¿Digite el nombre  porfavor?", title="validar nombre")
            self.enombre.focus_set()
        else:
            m=messagebox.askquestion(message="¿Desea Guardar el registro?", title="Guardar")
            if m=="yes":
                perso=Persona(self.enombre.get(),self.etelefono.get(),self.eemail.get(),self.etipo.get(),self.eestado.get())
                INSERTAR='INSERT INTO persona VALUES(null,%s,%s,%s,%s,%s)'
                dato=[perso.nombre,perso.telefono,perso.email,perso.estado,perso.tipo]
                Persona_D.insertar(INSERTAR,dato)
                messagebox.showinfo(message="¿Se guardo correctamente el registro?", title="Guardar persona")
            else:
                messagebox.showinfo(message="¿El registro no se guardo?", title="Guardar persona")