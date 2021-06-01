from tkinter import *
from tkinter import ttk

#ventana
wn = Tk()
wn.geometry('500x200')
wn.title('Toma de ramos')

#frases
frase1 = Label(wn, text="Buenas tardes")
frase1.grid(column=1, row=0)

#respuesta
def respuesta():
    frase1.configure(text='Quedaste en el cupo 348 :D')

#botones  
boton1 = Button(wn, text='Toma seccion de Programacion', command=respuesta, bg="pink", fg="red")    #boton para saludar
boton1.grid(column=5, row=0)

botonS = Button(wn, text='Salir',command=quit, bg="black", fg="red")    #boton para cerrar 
botonS.grid(column=10, row=10)


wn.mainloop() 