from tkinter import *
from tkinter import ttk

def mostrar():
    print("Hola Mundo")

raiz = Tk()
raiz.geometry("300x200") #Tamaño de la ventana
raiz.configure(bg="beige") #color de la ventana
raiz.title("aplication") #titulo de la ventana
boton1 = ttk.Button(raiz, text="salir", command=quit)  #insertar el boton en la ventana
boton1.pack(side=BOTTOM) #lugar en donde quiero que aparezca el boton
boton2 = ttk.Button(raiz, text="otro", command=mostrar)
boton2.pack(side=TOP)
etiquetas = Label(None,text="Hola Mundo", fg= "firebrick").pack() #Metodo 1 para insertar texto
etiqueta = ttk.Label(raiz, text= "Hola Mundo") #Metodo 2 para insertar texto
etiqueta.pack(side=TOP)
raiz.mainloop()

