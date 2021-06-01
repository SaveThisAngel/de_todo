import os

os.system("cls")

print ('''
###################################################
##         Números Palindromos.                  ##
##                                               ##
##   Número que se lee de izquierda a derecha    ##
##     igual que de derecha a izquierda          ##
###################################################
''')

numero = int(input("Ingrese un número postivo: "))

if numero >= 0:
    if str(numero) == str(numero)[::-1]:
        print("%i Es palindromo. " % numero)
    else:
        print("%i No es palindromo. " % numero)
else:
    print("El número tiene que ser positivo")