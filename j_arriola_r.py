import tkinter as tk
from tkinter import *
from tkinter import ttk

suma=0
cantidadprimos=0
cantidadnoprimos=0
cantidadnumeros=0
limite=0
def validar():
    raiz.geometry("580x370")
    global limite
    global cantidadnumeros
    global suma
    global cantidadprimos
    global cantidadnoprimos
    limite=limite+1
    novalido_lbl.configure(text="")
    ok=True
    d=2
    cantidadnumeros=cantidadnumeros+1
    while d<int(numero_entry.get()):
        resto = int(numero_entry.get())%d
        if resto == 0:
            ok = False
        d=d+1
    if ok==True and int(numero_entry.get())!=1:
        check_primo.select()
        check_noprimo.deselect()
        suma=suma+int(numero_entry.get())
        cantidadprimos=cantidadprimos+1
    else:
        check_noprimo.select()
        check_primo.deselect()
        cantidadnoprimos=cantidadnoprimos+1
    muestra_suma_primos_lbl.configure(text=str(suma))
    

def limpiar():
    raiz.geometry("580x370")
    global limite
    global cantidadnumeros
    global suma
    global cantidadprimos
    global cantidadnoprimos
    limite=0
    novalido_lbl.configure(text="")
    suma=0
    cantidadprimos=0
    cantidadnoprimos=0
    cantidadnumeros=0
    numero_entry.delete(0,END)
    numero_entry.insert(0,"0")
    check_primo.deselect()
    check_noprimo.deselect()
    muestra_suma_primos_lbl.configure(text="0")

def siguiente():
    raiz.geometry("580x370")
    novalido_lbl.configure(text="")
    numero_entry.delete(0,END)
    check_primo.deselect()
    check_noprimo.deselect()

def nueva_ventana():
    if 3<=limite and limite<=10000:
        nven = tk.Toplevel(raiz)
        nven.title("Resultados")
        nven.geometry("400x400")
        nven.configure(bg="light blue")
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
        numero_entry.delete(0,END)
    else:
        raiz.geometry("780x370")
        novalido_lbl.configure(text="Ingrese cantidad valida de numeros (entre 3 y 10.000)")

if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.title("Validador numeros primos")
    raiz.geometry("580x370")
    raiz.configure(bg = "light blue")
    raiz.resizable(True, True)
    suma_primos_lbl = ttk.Label(raiz, text = "Suma: ", foreground="black",background="cornflower blue",font=('Helvetica', 12, 'bold'))
    suma_primos_lbl.grid(row = 1, column = 1, padx = 10, pady = 10) 
    muestra_suma_primos_lbl = ttk.Label(raiz, text = "0",font=('Helvetica', 12, 'bold'))
    muestra_suma_primos_lbl.grid(row = 1, column = 2, padx = 10, pady = 10)   
    novalido_lbl = ttk.Label(raiz, text = "",foreground="red",background="light blue",font=('Helvetica', 12, 'bold'))
    novalido_lbl.grid(row = 4, column = 2, padx = 0, pady = 10) 
    numero_lbl = ttk.Label(raiz, text = "Numero: ", foreground="black",background="cornflower blue",font=('Helvetica', 12, 'bold'))
    numero_lbl.grid(row = 2, column = 1, padx = 10, pady = 10)
    numero = tk.StringVar()
    numero_entry = ttk.Entry(raiz, width = 20, textvariable = numero)
    numero_entry.grid(row = 2, column = 2)
    numero_entry.insert(0,"0")
    boton_validar=ttk.Button(raiz, text ="Validar", command = validar)
    boton_validar.grid(row = 3, column = 1, padx = 10, pady = 10)
    boton_limpiar=ttk.Button(raiz, text ="Limpiar", command = limpiar)
    boton_limpiar.grid(row = 4, column = 1, padx = 10, pady = 10)
    boton_siguiente=ttk.Button(raiz, text ="Siguiente numero", command = siguiente)
    boton_siguiente.grid(row = 3, column = 2, padx = 10, pady = 10)
    boton_finalizar=ttk.Button(raiz, text ="Finalizar", command = nueva_ventana)
    boton_finalizar.grid(row = 3, column = 3, padx = 10, pady = 10) 
    frame=tk.LabelFrame(raiz,background="light blue",text="Tipo de numero",font=('Helvetica', 10, 'bold'))
    frame.grid(row=2,column=4)
    check_primo=tk.Checkbutton(frame, text ="Es primo",state=DISABLED)
    check_primo.grid(row = 1, column = 4, padx = 10, pady = 10) 
    check_noprimo=tk.Checkbutton(frame, text ="No es primo",state=DISABLED)
    check_noprimo.grid(row = 2, column = 4, padx = 10, pady = 10) 
    imagen=PhotoImage(file="escudo.png")
    ttk.Label(raiz,image=imagen).grid(row=4,column=4) 
    raiz.mainloop()