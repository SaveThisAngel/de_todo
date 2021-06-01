from tkinter import tk

raiz = Tk()
raiz.title("Ventana Raiz o Principal")
raiz.geometry("500x300")
raiz.configure(bg = "beige")
raiz.resizable(True, True)
boton_nueva_ventana=ttk.Button(raiz, text ="Abrir Nueva Ventana", command = nueva_ventana)
boton_nueva_ventana.pack(pady = 30)


def nueva_ventana():
    hija = tk.Toplevel(raiz)
    hija.title("Ventana Hija")
    hija.geometry("400x400")
    hija.configure(bg="white")
    hija.resizable(True, True)
    etiqueta_hija = ttk.Label(hija, text = "Ventana Hija")
    boton_hija = ttk.Button(hija, text="Boton Hija")
    boton_hija.pack(pady = 40)

raiz.mainloop()