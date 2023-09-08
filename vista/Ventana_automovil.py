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
from Marca import Marca
from Personas import Persona
from Modelos import Modelos 
from Hijos_D import Marca_D
from Hijos_D import Color_D
from Hijos_D import Modelo_D
from Hijos_D import Persona_D
class Ventana_Automovil(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        global texto
        texto=StringVar()
        #*************************************configurar ventana***********************
        self.config(background="white")
        self.title("Ventana Automovil")
        self.geometry("550x300")
        
        self.lidpersona=Label(self,text="Cedula:",font=("Roboto Cn",12),bg="white")
        self.lidpersona.grid(row=0,column=0,pady=10,padx=10,sticky="w")

        self.lnombre=Label(self,text="Nombre:",font=("Roboto Cn",12),bg="white")
        self.lnombre.grid(row=1,column=0,pady=10,padx=10,sticky="w")


        self.lplaca=Label(self,text="Placa:",font=("Roboto Cn",12),bg="white")
        self.lplaca.grid(row=2,column=0,pady=10,padx=10,sticky="w")

        self.lidmarca=Label(self,text="Marca:",font=("Roboto Cn",12),bg="white")
        self.lidmarca.grid(row=3,column=0,pady=10,padx=10,sticky="w")
        

        self.lidmodelo=Label(self,text="Modelo",font=("Roboto Cn",12),bg="white")
        self.lidmodelo.grid(row=3,column=2,pady=10,padx=10,sticky="w")
    

        self.lidcolor=Label(self,text="Color",font=("Roboto Cn",12),bg="white")
        self.lidcolor.grid(row=4,column=0,pady=10,padx=10,sticky="w")

        self.lestado=Label(self,text="Estado",font=("Roboto Cn",12),bg="white")
        self.lestado.grid(row=4,column=2,pady=10,padx=10,sticky="w")
        
#********************************Entradas**************************************
        """
        entrada_id_p=ttk.Combobox(lblFrame_personauto,width=13,font=("Roboto Cn",12))
        entrada_id_p.grid(row=0,column=1,padx=5)
        dato=Persona_D.consultaidpersona()
        entrada_id_p["value"]=dato
        entrada_id_p.current(0)
        entrada_id_p.bind("<<ComboboxSelected>>",ejecutanombre)
        entrada_nombress=Entry(lblFrame_personauto,textvariable=texto,width=17,font=("Roboto Cn",12))
        """
    
#**********************************************************************************
        SELECCIONARDOS='SELECT id_persona FROM persona ORDER BY id_persona'
        dato=Persona_D.consultar(SELECCIONARDOS)
        self.eidpersona=ttk.Combobox(self,width=13,font=("Roboto Cn",12))
        self.eidpersona.grid(row=0,column=1,padx=5)
        self.eidpersona["value"]=dato
        self.eidpersona.current(0)
        self.eidpersona.bind("<<ComboboxSelected>>",self.ejecutanombre)

        self.enombre=Entry(self,textvariable=texto,font=("Roboto Cn",12),width=45,bd=2)
        self.enombre.grid(row=1,column=1,columnspan=3)
        """
        self.eplaca=Entry(self,font=("Roboto Cn",12),width=17,bd=2)
        self.eplaca.grid(row=2,column=1)

        dato2=Marca_D.consultar()
        self.eidmarca=ttk.Combobox(self,font=("Roboto Cn",12),width=15)
        self.eidmarca.grid(row=3,column=1)
        self.eidmarca["value"]=["mercedes","mazda"]

        self.eidmodelo=ttk.Combobox(self,font=("Roboto Cn",12),width=15)
        self.eidmodelo.grid(row=3,column=3)
        self.eidmodelo["value"]=["2021","2023"]

        self.eidcolor=ttk.Combobox(self,font=("Roboto Cn",12),width=15)
        self.eidcolor.grid(row=4,column=1)
        self.eidcolor["value"]=["Rojo","Verde"]
        """
        self.eestado=ttk.Combobox(self,font=("Roboto Cn",12),width=15)
        self.eestado.grid(row=4,column=3)
        self.eestado["value"]=["Activo","Inactivo"]
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
#*********************************Botones**************************************
        self.buscar=Button(self,image=self.imbuscar,borderwidth=0,bg="white")
        self.buscar.place(x=300,y=85)
        self.bguardar=Button(self,image=self.imguardar,borderwidth=0,command=self.guardarautomovil)
        self.bguardar.place(x=50,y=230)
        self.bmodificar=Button(self,image=self.imeditar,borderwidth=0,bg="white")
        self.bmodificar.grid(row=5,column=1,pady=10)
        self.beliminar=Button(self,image=self.imeliminar,borderwidth=0,bg="white")
        self.beliminar.grid(row=5,column=2,pady=10)
        self.bsalir=Button(self,image=self.imsalir,command=self.destroy,borderwidth=0,bg="white")
        self.bsalir.grid(row=5,column=3,pady=10)
        self.focus()
        self.grab_set() 
    def ejecutanombre(self,event=None):
        global texto
        persona1=Persona(id_persona=self.eidpersona.get())
        dato=(persona1.id_persona,)
        SELECCIONATRES='SELECT nombre FROM persona  where id_persona=%s '
        persona=Persona_D.consultardos(SELECCIONATRES,dato)
        print(persona)
        for i in persona:
            texto.set(i[0])
        #self.eplaca.focus_set()
#********************************Guarda Automovil***********************************   
    def guardarautomovil(self):
        if self.eplaca.get()==" ":
            messagebox.showinfo(message="¿Digite el nombre  porfavor?", title="validar placa")
            self.eplaca.focus_set()
        else:
            m=messagebox.askquestion(message="¿Desea Guardar el registro?", title="Guardar")
            if m=="yes":
                auto=Automovil(self.eplaca.get(),self.eidmarca.get(),self.eidmodelo.get(),self.eidcolor.get(),self.eestado.get(),self.eidpersona.get())
                INSERTAR='INSERT INTO automovil VALUES(null,%s,%s,%s,%s,%s)'
                dato=[auto.placa,auto.id_marca,auto.id_modelo,auto.id_color,auto.estado,auto.id_persona]
                Automovil_D.insertar(INSERTAR,dato)
                messagebox.showinfo(message="¿Se guardo correctamente el registro?", title="Guardar Automovil")
            else:
                messagebox.showinfo(message="¿El registro no se guardo?", title="Guardar Automovil")
"""
#***************************************************************************
    
#************************************************************************
    
    def ejecutamarca(event=None):
        marca1=Marca(marca=emarca.get())
        marcass=Marca_D.consultamarca(marca1)
        for i in marcass:
            marcarespuesta.set(i[0])

#***************************************************************************
        
#*******.********************************************************************
        emarca=ttk.Combobox(self,textvariable=marca1,width=13,font=("Roboto Cn",12))
        emarca.grid(row=2,column=1,padx=10)
        emarca["value"]=dato2
        emarca.current(0)
        emarca.bind("<<ComboboxSelected>>",ejecutamarca)
        emarca=Entry(self,textvariable=marcarespuesta)#respuestas
#********************************imagenes de los botones*********************
        
    #********************************************Validar automovil *******************************************

    def validaplacautomovil(event=None):
        a=set(eplaca.get())
        vali=elaca.get()
        if (is_empty(a)==True):
            messagebox.showinfo(message="¿Digite la placa porfavor?", title="validar placa")
            eplaca.focus_set()
        elif (vali.isalnum()==False):
            messagebox.showinfo(message="¿Digite  tres Letras y tres numeros?", title="validar placa")
            eplaca.delete(0,END)
            eplaca.focus_set()
        else:
            activarlabelyentradasdelautomovil()
            auto1=Automovil(id_persona=entrada_id_p.get(),placa=eplaca.get())
            auto2=Automovil_D.validaplaca(auto1)
        if auto2==[]:
            messagebox.showinfo(message="¿la placa no esta registrada en el sistema?", title="Validar placa")
            entrada_marca.focus_set()
        else:
            messagebox.showinfo(message="¿la placa  esta registrada en el sistema?", title="Validar placa")
            for i in auto2:
                marca1.set(i[0])
                color1.set(i[1])
                modelo1.set(i[2])
                estado1.set(i[3])
                marcarespuesta.set(i[4])
                colorespuesta.set(i[5])
                modelorespuesta.set(i[6])
            boton_guardar_automovil.config(state=DISABLED)
            boton_modificar_automovil.config(state=NORMAL)
            boton_eliminar_automovil.config(state=NORMAL)
            entrada_placa.focus_set()

"""