import os
os.system("cls")

print ('''
###################################################
##              Nmeros Primos.                  ##
##                                               ##
##     Numero que son divisibles por 1           ##
##            y por si mismo                     ##
###################################################
''')

print("Define el rango ")

a = int(input("Número menor: "))
b = int(input("Número mayor: "))
print("#########################")
     
for numero in range(a,b):
    if (numero == 1):
        pass
    else:
        for i in range(2,numero):
            if (numero%i == 0):
                break
        else:
            print(numero, "Es primo")