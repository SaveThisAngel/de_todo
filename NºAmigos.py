import os

os.system("cls")

print ('''
###################################################
##              Números Amigos.                  ##
##                                               ##
##   La suma de los divisores de un número es    ##
##      igual al otro número y viceversa         ##
###################################################
''')

def numeros_amigos(a,b):
    suma_a = 0
    suma_b = 0
    for i in range(1,a):
        if a%i == 0:
            suma_a += i
                                                 
    for k in range(1,b):
        if b%k == 0:
            suma_b += k
 
    return suma_a == b and suma_b == a
 
numero_1 = int(input("Introduzca el primer número: "))
numero_2 = int(input("Introduzca el segundo número: "))
 
if numeros_amigos(numero_1,numero_2):
    print ("Son amigos")
else:
    print ("No son amigos")