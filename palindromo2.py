"""
numero = int(input("ingrea un numero: "))

centena = (numero/100)
decena = ((numero%100) /10)
unidad = ((numero%100) %10)

if (centena == unidad):
    print ("el numero no palindromo")
else:
    print ("el numero si es palindromo")    

"""

print ('''
###################################################
##         Numeros Palindromos.                  ##
##                                               ##
##   Numero que se lee de izquierda a derecha    ##
##     igual que de derecha a izquierda          ##
###################################################
''')

numero = int(input("ingrese un numero postivo: "))

if numero >= 0:
    if str(numero) == str(numero)[::-1]:
        print("%i es palindromo. " % numero)
    else:
        print("%i No es palindromo. " % numero)


else:
    print("El numero tiene que ser positivo")