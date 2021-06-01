'''
from tkinter import *
from tkinter import messagebox
top =Tk()
top.geometry("100x100")
messagebox.showinfo("Hola","Eri gei ?")
top.mainloop()
'''


'''
from tkinter import *
from tkinter import messagebox
top =Tk()
top.geometry("100x100")
messagebox.showinfo("information","Information")
top.mainloop()

'''

from tkinter import *
from tkinter import messagebox

wn = Tk()

result1 = messagebox.showinfo("Crear cuenta", "¿De verdad quieres crear una cuenta? ")


#print(result1) #Si = True , No = False

'''
result2 = messagebox.askyesno("Confirmacion", "¿De verdad quieres continuar? ")
print(result2) #Si = True , No = False

result3 = messagebox.askyesnocancel("Estás a punto de entrar en la página de creación", "¿Estás listo para continuar? ")
print(result3) #Si = True , No = False , cancelar = None
'''

'''
messagebox.showinfo("Mensaje", "Un mensaje de Tk")
messagebox.showwarning("Precaucion", "Advertencia de Tk")
messagebox.showerror("Error", "Error de Tk")
'''


'''
from tkinter import *
from tkinter import messagebox

wn = Tk()
wn.iconbitmap("gallina.ico")

def mensaje():
    respuesta = messagebox.askquestion("Mensaje", "Hola mundo!")
    Label(wn, text=respuesta).pack()
    

Button(wn, text="Pregunta", command=mensaje).pack()


wn.mainloop()
'''
