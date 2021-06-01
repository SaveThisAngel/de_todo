"""
def amigos (primero, segundo):
    contador = 1
    
    primero1 = int(input("Primer numero: "))            
    segundo2 = int(input("Segundo numero: "))

        while(contador <= primero):
            if primero%contador == 0:
                if amigos (primero, segundo):
                    print ("los numeros que ingresaste (",primero1, "y", segundo2, ") son amigos")
                else:
                    print ("los numeros que ingresaste (",primero1, "y", segundo2, ") no son amigos")    

"""   
"""               
import os

os.system("cls")

print ('''
###################################################
##              Numeros Amigos.                  ##
##                                               ##
##   La suma de los divisores de un numero es    ##
##      igual al otro numero y viceversa         ##
###################################################
''')

def suma(n1,n2):
       for i in range(4,n2):
             if (n2 % i == 0):
                    n1 = n1 + i
       return n1

suma_1 = 1
suma_2 = 1
suma_3 = 1
suma_4 = 1
numero_1 = int(input("ingrese primer numero: "))
numero_2 = int(input("ingrese segundo numero: "))
numero_3 = int(input("ingrese tercer numero: "))
numero_4 = int(input("ingrese cuarto numero: "))
suma_1 = suma(numero_1, suma_1)
suma_2 = suma(numero_2, suma_2)
suma_3 = suma(numero_3, suma_3)
suma_4 = suma(numero_4, suma_4)
if ((suma_1 == numero_2) and (suma_2 == numero_1) and (suma_3 == numero_4) and (suma_4 == numero_3)):
       print("los numeros " + str(numero_1) +" y " + str(numero_2) + " y " +  str(numero_3) + " y " +  str(numero_4) +" son amigos")
else:
       print("los numeros "+ str(numero_1) + " y " + str(numero_2) + " y " +  str(numero_3) + " y " +  str(numero_4) +" No son numeros amigos")

"""

"""

def suma(n1,n2):
       for i in range(2,n1):
             if (n1 % i == 0):
                    n2 = n2 + i
       return n2
suma_1 = 1
suma_2 = 1

numero_1 = int(input("ingrese primer numero: "))
numero_2 = int(input("ingrese segundo numero: "))

suma_1 = suma(numero_1, suma_1)
suma_2 = suma(numero_2, suma_2)

if ((suma_1 == numero_2) and (suma_2 == numero_1)):
       print("los numeros " + str(numero_1) +" y " + str(numero_2) + " Son numeros amigos")
else:
       print("los numeros "+ str(numero_1) + " y " + str(numero_2) +" No son numeros amigos")
"""

import os

os.system("cls")

print ('''
###################################################
##              Numeros Amigos.                  ##
##                                               ##
##   La suma de los divisores de un numero es    ##
##      igual al otro numero y viceversa         ##
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
 
numero_1 = int(input("Introduzca el primer numero: "))
numero_2 = int(input("Introduzca el segundo numero: "))
 
if numeros_amigos(numero_1,numero_2):
    print ("Son amigos")
else:
    print ("No son amigos")
    