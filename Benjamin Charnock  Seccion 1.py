# Autor : Benjamin Charnock Verdugo
# Seccion: 1
# Asignatura: Programacion
# Carrera: Ingenieria Civil Informatica
# Nombre del problema: CUENTA PRIMOS


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import time

win = tk.Tk()
win.title("CUENTA PRIMOS")
win.geometry("450x350")
win.configure(bg = "darkviolet")
win.resizable(False, False)
win.iconbitmap("gallina.ico")

def validar():
    global limite
    global cantidad_numeros
    global suma
    global cantidad_primos
    global cantidad_no_primos
    limite = limite + 1
    ok = True
    d = 2
    cantidad_numeros = cantidad_numeros + 1
    while d < int(numero_entry.get()):
        resto = int(numero_entry.get())%d
        if resto == 0:
            ok = False
        d = d + 1
    if ok == True and int(numero_entry.get())!=1:
        check_primo.select()
        check_noprimo.deselect()
        suma = suma + int(numero_entry.get())
        cantidad_primos = cantidad_primos + 1
    else:
        check_noprimo.select()
        check_primo.deselect()
        cantidad_no_primos = cantidad_no_primos + 1
    muestra_suma_primos_lbl.configure(text=str(suma))

def mensaje():
    #messagebox.showinfo("Informacion, Autor: Benjamin Charnock")
    messagebox.showinfo("Acerca de", "Autor: Benjamin Charnock")
    messagebox.showinfo("Carrera", "Ingenieria Civil Informatica")
    messagebox.showinfo("Seccion", "Seccion 123")
    

menu_g = tk.Menu(win)

menu1 = tk.Menu(menu_g, tearoff = 0)
menu1.add_command(label ='Autor', command = mensaje)

menu2 = tk.Menu(menu_g, tearoff= 0)
menu2.add_command(label = '-----')

menu_g.add_cascade(label = 'Acerca de', menu = menu1)
menu_g.add_cascade(label = 'Ayuda', menu = menu2)

check = tk.LabelFrame(win,background = "blueviolet")
check.place(x=320, y=5, width=120, height=100)
check_primo = tk.Checkbutton(check, text ="Es primo",state=DISABLED)
check_primo.grid(row = 1, column = 4, padx = 10, pady = 10) 
check_noprimo = tk.Checkbutton(check, text ="No es primo",state=DISABLED)
check_noprimo.grid(row = 2, column = 4, padx = 10, pady = 10) 

suma = 0
cantidad_primos = 0 
cantidad_no_primos = 0
cantidad_numeros = 0
limite = 0


def nueva_ventana():
    win2 = tk.Toplevel(win)
    win2.title("Resultados")
    win2.geometry("300x200")
    win2.configure(bg="purple")
    win2.resizable(False, False)    

    lbl_suma = ttk.Label(win2, text = "Suma primos",background="darkorchid",foreground="white")
    lbl_suma.grid(row = 1, column = 1, padx = 10, pady = 10) 
    lbl_suma = ttk.Label(win2, text = str(suma),background="darkorchid",foreground="white")
    lbl_suma.grid(row = 1, column = 2, padx = 10, pady = 10)
    
    lbl_cantidad_primos=ttk.Label(win2,text="Cantidad numeros primos leidos",background="darkorchid",foreground="white")
    lbl_cantidad_primos.grid(row = 2, column = 1, padx = 10, pady = 10)
    lbl_cantidad_primos=ttk.Label(win2,text=str(cantidad_primos),background="darkorchid",foreground="white")
    lbl_cantidad_primos.grid(row = 2, column = 2, padx = 10, pady = 10)
    
    lbl_cantidad_nprimos=ttk.Label(win2,text="Cantidad numeros no primos leidos",background="darkorchid",foreground="white")
    lbl_cantidad_nprimos.grid(row = 3, column = 1, padx = 10, pady = 10)
    lbl_cantidad_nprimos=ttk.Label(win2,text=str(cantidad_no_primos),background="darkorchid",foreground="white")
    lbl_cantidad_nprimos.grid(row = 3, column = 2, padx = 10, pady = 10)
    
    lbl_cantidad_nprimos=ttk.Label(win2,text="Cantidad numeros leidos",background="darkorchid",foreground="white")
    lbl_cantidad_nprimos.grid(row = 4, column = 1, padx = 10, pady = 10)
    lbl_cantidad_nprimos=ttk.Label(win2,text=str(cantidad_numeros),background="darkorchid",foreground="white")
    lbl_cantidad_nprimos.grid(row = 4, column = 2, padx = 10, pady = 10)

def siguiente():
    numero_entry.delete(0,END)


suma_primos_lbl = ttk.Label(win, text = "Suma: ", foreground="black",background="violetred")
suma_primos_lbl.grid(row = 1, column = 1, padx = 10, pady = 10) 
muestra_suma_primos_lbl = ttk.Label(win, text = "0")
muestra_suma_primos_lbl.grid(row = 1, column = 2, padx = 10, pady = 10)   

numero_lbl = ttk.Label(win, text = "Numero: ", foreground="black",background="violetred")
numero_lbl.grid(row = 2, column = 1, padx = 10, pady = 10)
numero = tk.StringVar()
numero_entry = ttk.Entry(win, width = 20, textvariable = numero)
numero_entry.grid(row = 2, column = 2)

boton_validar=ttk.Button(win, text ="Validar", command = validar)
boton_validar.grid(row = 3, column = 1, padx = 10, pady = 10)
boton_siguiente=ttk.Button(win, text ="Siguiente numero", command = siguiente)
boton_siguiente.grid(row = 3, column = 2, padx = 10, pady = 10)
boton_finalizar=ttk.Button(win, text ="Finalizar", command = nueva_ventana)
boton_finalizar.grid(row = 3, column = 3, padx = 10, pady = 10) 


def link():
    webbrowser.open_new_tab("https://portal.ucm.cl/")


imagen = PhotoImage(file='escudo.png')
boton_imagen = boton0 = Button(win, width=200, height=160, image= imagen, bg = 'white', command= link)
boton0.place(x=125, y=150)
    
pagina_lbl = ttk.Label(win, text = "Ir a la UCM: ", foreground="black",background="violetred")
pagina_lbl.place(x=50, y=200)

win.config(menu=menu_g)  
win.mainloop()
