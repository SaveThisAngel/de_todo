def es_primo(numero):
    if numero <= 1:
        return False
    div= 0
    for i in range(1, (numero//2)+1):
        if numero %i == 0:
            div+=1
    if div <= 1:
        return True
    else:
        return False

numero=int(input("Ingrese un numero para ver si es primo:"))
result= es_primo(numero)
if result==False:
    print("El numero No es primo")
else:
    print("El numero Si es primo")    