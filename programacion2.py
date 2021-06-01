"""
a. Que retorne la cantidad de sobrevivientes.
b. Que retorne la cantidad de mujeres en el barco.
c. Que retorne la cantidad de hombres en el barco.
d. Que retorne la cantidad de pasajeros de primera clase.
e. Que retorne la cantidad de pasajeros de segunda clase.
f. Que retorne la cantidad de pasajeros de tercera clase.
g. Que retorne la cantidad de pasajeros que embarcaron en Cherburgo.
h. Que retorne la cantidad de pasajeros que embarcaron en Queenstown.
i. Que retorne la cantidad de pasajeros que embarcaron en Southampton

"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox


def lectura_datos(nombre):
    nombre = nombre.get()
    archivo = open(nombre)
    archivo.flush()
    mi_lista = []
    
    for linea in archivo:
        #linea = archivo.readline()
        linea = linea.rstrip("\n")
        lis = linea.split(",")
        #print(li[2]+ ', '+ lis[3])
        mi_lista.append(lis)
    archivo.close()

    sobrevivientes = cuantos_sobrevivientes(mi_lista)
    mBox.showinfo(message = sobrevivientes, title = 'Sobrevivientes')

def cuantos_sobrevivientes(lista):
    acumulador = 0
    for elem in lista:
        num = int(elem[1])
        if num == 1:
            acumulador = acumulador +1
    return acumulador              

def cuantas_mujeres(lista):
    acumulador = 0
    for elem in lista:
        if elem[4] =='female':
            acumulador = acumulador +1
    return acumulador

def cuantos_hombres(lista):
    acumulador = 0
    for elem in lista:
        if elem[4] =='male':
            acumulador = acumulador +1
    return acumulador



if __name__ == "__main__":
    wn = tk.Tk()
    wn.title("Titanic")
    wn.geometry("500x500")
    wn.resizable(True, True)
    
    pedir_archivo = ttk.Label(wn, text = "Nombre Archivo: ")
    pedir_archivo.grid(row = 1, column = 1)

    archivo = tk.StringVar()
    nombre_archivo = ttk.Entry(wn, width = 20, textvariable = archivo)
    nombre_archivo.grid(row = 1, column = 2)

    buscar_datos = ttk.Button(wn, text = "Procesar", command = lambda:lectura_datos(archivo))
    buscar_datos.grid(row = 4, column = 2)
    wn.mainloop()