import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import ttk
import tkinter as tk

suma=0
cantidadprimos=0
cantidadnoprimos=0
cantidadnumeros=0

wn = Tk() 
wn.title("Validador de edad")
wn.geometry("500x350") 
wn.config(bg='cyan')

mensaje = Label(wn, text="Numeros primos", font=("arial", 15, "bold"),bg="green", fg="black").pack() 
suma = Label(wn, text="Suma: ", font=("arial", 20, "bold"), fg="green").place(x=10, y=100)
numero = Label(wn, text="Numero:", font=("arial", 20, "bold"), fg="green").place(x=10, y=200)


suma_entry = Entry(wn, width=25, bg="white") 
suma_entry.place(x=340, y=111) 
numero_entry = Entry(wn, width=25, bg="white")
numero_entry.place(x=340, y=210)


#def primo():
    

valid = Button(wn, text="Validar", width=30, height=5, bg="white").place(x=120, y=250) 

wn.mainloop() 

