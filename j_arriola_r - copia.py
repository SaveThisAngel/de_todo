import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import ttk
import tkinter as tk

suma=0
cantidadprimos=0
cantidadnoprimos=0
cantidadnumeros=0
def validar():
    global cantidadnumeros
    global suma
    global cantidadprimos
    global cantidadnoprimos
    ok=True
    d=2
    cantidadnumeros=cantidadnumeros+1
    while d<int(numero_entry.get()):
        resto = int(numero_entry.get())%d
        if resto == 0:
            ok = False
        d=d+1
    if ok==True:
        suma=suma+int(numero_entry.get())
        cantidadprimos=cantidadprimos+1
    else:
        cantidadnoprimos=cantidadnoprimos+1
    muestra_suma_primos_lbl.configure(text=str(suma))
    
def siguiente():
    numero_entry.delete(0,END)

def nueva_ventana():
    nven = tk.Toplevel(raiz)
    nven.title("Resultados")
    nven.geometry("400x400")
    nven.configure(bg="gray")
    nven.resizable(True, True)
    lbl_suma = ttk.Label(nven, text = "Suma primos",background="green",foreground="white")
    lbl_suma.pack(pady = 10)
    lbl_suma = ttk.Label(nven, text = str(suma),background="green",foreground="white")
    lbl_suma.pack(pady = 5)
    lbl_cantidad_primos=ttk.Label(nven,text="Cantidad numeros primos leidos",background="red",foreground="white")
    lbl_cantidad_primos.pack(pady = 10)
    lbl_cantidad_primos=ttk.Label(nven,text=str(cantidadprimos),background="red",foreground="white")
    lbl_cantidad_primos.pack(pady = 5)
    lbl_cantidad_nprimos=ttk.Label(nven,text="Cantidad numeros no primos leidos",background="blue",foreground="white")
    lbl_cantidad_nprimos.pack(pady = 10)
    lbl_cantidad_nprimos=ttk.Label(nven,text=str(cantidadnoprimos),background="blue",foreground="white")
    lbl_cantidad_nprimos.pack(pady = 5)
    lbl_cantidad_nprimos=ttk.Label(nven,text="Cantidad numeros leidos",background="yellow")
    lbl_cantidad_nprimos.pack(pady = 10)
    lbl_cantidad_nprimos=ttk.Label(nven,text=str(cantidadnumeros),background="yellow")
    lbl_cantidad_nprimos.pack(pady = 5)
    boton_ok = ttk.Button(nven, text="OK",command=nven.destroy)
    boton_ok.pack(pady = 20)

if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.title("Ventana Raiz o Principal")
    raiz.geometry("500x300")
    raiz.configure(bg = "cyan")
    raiz.resizable(True, True)
    suma_primos_lbl = ttk.Label(raiz, text = "Suma: ", foreground="black",background="yellow")
    suma_primos_lbl.grid(row = 1, column = 1, padx = 10, pady = 10) 
    muestra_suma_primos_lbl = ttk.Label(raiz, text = "0")
    muestra_suma_primos_lbl.grid(row = 1, column = 2, padx = 10, pady = 10)   
    numero_lbl = ttk.Label(raiz, text = "Numero: ", foreground="black",background="yellow")
    numero_lbl.grid(row = 2, column = 1, padx = 10, pady = 10)
    numero = tk.StringVar()
    numero_entry = ttk.Entry(raiz, width = 20, textvariable = numero)
    numero_entry.grid(row = 2, column = 2)
    boton_validar=ttk.Button(raiz, text ="Validar", command = validar)
    boton_validar.grid(row = 3, column = 1, padx = 10, pady = 10)
    boton_siguiente=ttk.Button(raiz, text ="Siguiente numero", command = siguiente)
    boton_siguiente.grid(row = 3, column = 2, padx = 10, pady = 10)
    boton_finalizar=ttk.Button(raiz, text ="Finalizar", command = nueva_ventana)
    boton_finalizar.grid(row = 3, column = 3, padx = 10, pady = 10) 
    
    raiz.mainloop()