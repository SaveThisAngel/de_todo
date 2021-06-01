from tkinter import *

wn = Tk()
wn.title('Calculadora')
wn.iconbitmap("gallina.ico")

#Valor principal

i = 0

#Entrada

texto = Entry(wn, font= ('Calibri 20'))
texto.grid(row = 0, column = 0, columnspan = 6, padx = 5, pady = 5)


#Funciones

def click(valor):
    global i
    texto.insert(i, valor)
    i += 1

def borrar():
    texto.delete(0, END)
    i = 0

def operacion():
    ecuacion = texto.get()
    resultado = eval(ecuacion)
    texto.delete(0, END)
    texto.insert(0, resultado)
    i = 0

#Botones

boton1 = Button(wn, text = '1', width = 5, height = 2, command = lambda: click(1))
boton2 = Button(wn, text = '2', width = 5, height = 2, command = lambda: click(2))
boton3 = Button(wn, text = '3', width = 5, height = 2, command = lambda: click(3))
boton4 = Button(wn, text = '4', width = 5, height = 2, command = lambda: click(4))
boton5 = Button(wn, text = '5', width = 5, height = 2, command = lambda: click(5))
boton6 = Button(wn, text = '6', width = 5, height = 2, command = lambda: click(6))
boton7 = Button(wn, text = '7', width = 5, height = 2, command = lambda: click(7))
boton8 = Button(wn, text = '8', width = 5, height = 2, command = lambda: click(8))
boton9 = Button(wn, text = '9', width = 5, height = 2, command = lambda: click(9))
boton0 = Button(wn, text = '0', width = 16, height = 2, command = lambda: click(0))

boton_borrar = Button(wn, text = 'AC', width = 5, height = 2, command = lambda: borrar())
boton_paren1 = Button(wn, text = '(', width = 5, height = 2, command = lambda: click('('))
boton_paren2 = Button(wn, text = ')', width = 5, height = 2, command = lambda: click(')'))
boton_punto = Button(wn, text = '.', width = 5, height = 2, command = lambda: click('.'))

boton_suma = Button(wn, text = '+', width = 5, height = 2, command = lambda: click('+'))
boton_resta = Button(wn, text = '-', width = 5, height = 2, command = lambda: click('-'))
boton_divi = Button(wn, text = '/', width = 5, height = 2, command = lambda: click('/'))
boton_mult = Button(wn, text = 'x', width = 5, height = 2, command = lambda: click('x'))
boton_igual = Button(wn, text = '=', width = 5, height = 2, command = lambda: operacion())

#Agregar botones

boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_paren1.grid(row = 1, column = 1, padx = 5, pady = 5)
boton_paren2.grid(row = 1, column = 2, padx = 5, pady = 5)
boton_divi.grid(row = 1, column = 3, padx = 5, pady = 5)

boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1, padx = 5, pady = 5)
boton9.grid(row = 2, column = 2, padx = 5, pady = 5)
boton_mult.grid(row = 2, column = 3, padx = 5, pady = 5)

boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1, padx = 5, pady = 5)
boton6.grid(row = 3, column = 2, padx = 5, pady = 5)
boton_suma.grid(row = 3, column = 3, padx = 5, pady = 5)

boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1, padx = 5, pady = 5)
boton3.grid(row = 4, column = 2, padx = 5, pady = 5)
boton_resta.grid(row = 4, column = 3, padx = 5, pady = 5)

boton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 3, padx = 5, pady = 5)



imagen = PhotoImage(file='awita.png')
boton_imagen = boton0 = Button(wn, width=150, height=35, image= imagen, bg = 'white')
boton0.grid(row = 6, column = 0, columnspan = 6, padx = 5, pady = 10)



wn.mainloop()