"""
from tkinter import *
from tkinter import messagebox

wn = Tk()
wn.geometry("200x200")
wn.title('nueva ventana')

def precionar():
	response = messagebox.showinfo("Mi mensaje", "Hola Mundo!")
	Label(wn, text=response).pack()

Button(wn, text="Preciona", command=precionar).pack()

mainloop()

"""
##########################################################
"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Codemy.com - Learn To Code!')
root.geometry("400x400")

def selected(event):
	#myLabel = Label(root, text=clicked.get()).pack()
	if clicked.get() == 'Friday':
		myLabel = Label(root, text="Yay! It's Friday").pack()
	else:
		myLabel = Label(root, text=clicked.get()).pack()


def comboclick(event):
	#myLabel = Label(root, text=myCombo.get()).pack()
	if myCombo.get() == 'Friday':
		myLabel = Label(root, text="Yay! It's Friday").pack()
	else:
		myLabel = Label(root, text=myCombo.get()).pack()


options = [
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday",
	"Sunday",
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options, command=selected)
drop.pack(pady=20)

myCombo = ttk.Combobox(root, value=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()


#myButton = Button(root, text="select from list", command=selected)
#myButton.pack()

root.mainloop()

"""
##########################################################
"""
from tkinter import *
from tkinter import ttk

wn = Tk()
wn.title('Crear ventana')
wn.geometry("500x500")


wn2 = ttk.Notebook(wn)
wn2.pack()

def ocultar():
	wn2.hide(1)

def mostrar():
	wn2.add(marco2, text="Ventana Roja")

def seleccionar():
	wn2.select(1)

marco1 = Frame(wn2, width=500, height=500, bg="blue")
marco2 = Frame(wn2, width=500, height=500, bg="red")

marco1.pack(fill="both", expand=1)
marco2.pack(fill="both", expand=1)

wn2.add(marco1, text="Ventana Azul")
wn2.add(marco2, text="Ventana Roja")

boton1 = Button(marco1, text="Eliminar ventana 2", command=ocultar).pack(pady=10)

boton2 = Button(marco1, text="Mostrar ventana 2", command=mostrar).pack(pady=10)

boton3 = Button(marco1, text="Navegar en la ventana 2", command=seleccionar).pack(pady=10)



wn.mainloop()

"""

list = 
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        newEmail = ""
        emailsCounter = {}
        foundPlus = True
        foundAt = False
        for email in emails:
            newEmail = ""
            foundPlus = True
            foundAt = False
            for letter in email:
                if letter == '+':
                    foundPlus = False
                    
                if letter == '@':
                    foundPlus = True
                    foundAt = True
                    
                if foundPlus:
                    if letter=='.' and foundAt == False:
                        pass
                    else:
                        newEmail+=letter
                        
            if emailsCounter.get(newEmail) == None:
                emailsCounter[newEmail] = 1
            else:
                emailsCounter[newEmail] += 1
        return len(emailsCounter)
