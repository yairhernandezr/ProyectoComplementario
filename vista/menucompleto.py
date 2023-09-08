from tkinter import * 
v=Tk()
v.geometry("400x200")
v.config(bg="gray17")
menuframe=Frame(v,bg="black")
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
menu_persona=Menu(persona,tearoff=0)
menu_persona.add_command(label="Registro",
						 command=lambda:print("hola"),
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
persona.config(menu=menu_persona)
persona.pack(side="left")
automovil.config(menu=menu_automovil)
automovil.pack(side="left")
v.mainloop()