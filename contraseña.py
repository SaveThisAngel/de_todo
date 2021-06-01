def intro_datos():
    contraseña = input("ingrese contraseña a guardar: ")
    return contraseña

def datos(contraseña):
    contraseña2 = input("ingrese la contraseña: ")
    if contraseña == contraseña2:
        print("contraseña incorrecta, ingrese nuevamente") 
    else:
        print("contraseña correcta")
        

def main():
    contraseña = intro_datos()
    datos(contraseña)

if __name__ == '__main__':
    main()                