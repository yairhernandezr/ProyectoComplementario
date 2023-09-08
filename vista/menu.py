import tkinter as tk
from tkinter import ttk 
v=tk.Tk()
v.geometry("500x500")
treeview=ttk.Treeview()
item=treeview.insert("",tk.END,text="Automovil")
treeview.insert(item,tk.END,text="Marca")
treeview.insert(item,tk.END,text="Modelo")
treeview.insert(item,tk.END,text="Color")
item2=treeview.insert("",tk.END,text="Persona")
treeview.insert(item2,tk.END,text="Registrar")
treeview.grid(row=0,column=0)
v.mainloop()

