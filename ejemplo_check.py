import tkinter as tk
from tkinter import ttk
from tkinter import *

def seleccionar():
    cadena = ""
    if (leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"

    if (azucar.get()):
        cadena += " y con azúcar"
    else:
        cadena += " y sin azúcar"
    
    if azucar.get() and leche.get():
        otro.set(True)
    else:
        otro.set(False)
    monitor.config(text=cadena)

if __name__ == "__main__":
    # Configuración de la raíz
    root = Tk()
    root.title("Cafetería")
    root.config(bd=15)

    leche = IntVar()    # 1 si, 0 no
    azucar = IntVar()   # 1 si, 0 no

    #imagen = PhotoImage(file="cafe_1.png")
    #eti_cafe = tk.Label(root, image=imagen)
    #eti_cafe.pack(side="left")

    frame = tk.Frame(root)
    frame.pack(side="left")

    eti_pregunta = tk.Label(frame, text="¿Cómo quieres el café?")
    eti_pregunta.pack(anchor="w")
    leche_check = tk.Checkbutton(frame, text="Con leche", variable=leche, onvalue=1, offvalue=0, command=seleccionar)
    leche_check.pack(anchor="w")
    azucar_check = tk.Checkbutton(frame, text="Con azúcar", variable=azucar, onvalue=1,offvalue=0, command=seleccionar)
    azucar_check.pack(anchor="w")
    
    otro = IntVar()
    otro_check = tk.Checkbutton(frame, text="Ambos ...", variable = otro, state = DISABLED)
    otro_check.pack(anchor="w")
    monitor = tk.Label(frame)
    monitor.pack()

    # Finalmente bucle de la aplicación
    root.mainloop()