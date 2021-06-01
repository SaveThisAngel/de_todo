
import tkinter as tk
from tkinter import *


win = tk.Tk()
win.title("CUENTA PRIMOS")
win.geometry("450x350")
win.configure(bg = "darkviolet")
win.resizable(False, False)
win.iconbitmap("gallina.ico")

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
