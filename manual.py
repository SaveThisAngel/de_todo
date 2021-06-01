from tkinter import * 
from tkinter import messagebox

wn = Tk() 
wn.title("Validador de edad")
wn.geometry("500x350") 
wn.config(bg='cyan')

mensaje = Label(wn, text="Veamos si tienes la edad adecuada", font=("arial", 15, "bold"),bg="green", fg="black").pack() 
nombre = Label(wn, text="Introduce tu nombre: ", font=("arial", 20, "bold"), fg="green").place(x=10, y=100)
edad = Label(wn, text="Introduce tu edad:", font=("arial", 20, "bold"), fg="green").place(x=10, y=200)


nombre_entry = Entry(wn, width=25, bg="white") 
nombre_entry.place(x=340, y=111) 
edad_entry = Entry(wn, width=25, bg="white")
edad_entry.place(x=340, y=210)


def comprobar_edad(): 

    if (int(edad_entry.get() or 0) >=18) and (int(edad_entry.get() or 0) <=30):
        messagebox.showinfo("Felicitaciones!", "Bienvenidos a las vacaciones para personas de entre 18 y 30 años, " + nombre_entry.get() +"!"  " Buen viaje")
    else:
        messagebox.showinfo("Error", "Perdon " + nombre_entry.get() + ", no estás dentro del rango de edad")

comprobar = Button(wn, text="Validar", width=30, height=5, bg="white", command= comprobar_edad).place(x=120, y=250) 

wn.mainloop() 