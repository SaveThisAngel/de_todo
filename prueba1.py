'''
a = 0

b = [0, 1, 2]

a = 1

b[0] = 1

print (a, " - ", b)
'''


'''
lista1 = [1, 2, 3]

lista2 = [1, 2, 3]

i = 0

while i < len(lista2):

    lista1.append (lista2[i])

    i = i + 1

lista2 = lista2 + [4]

lista1[-1] = 100

lista3 = lista2[:]

print (lista3)
'''

'''

from math import sqrt

s = 4

a = s-1

b = s

c = s+1

s = (a + b + c) / 2.0

z = sqrt(s * (s-a) * (s-b) * (s-c))

print (z, "-", s)

'''

'''

def modifica (a, b):

    for elemento in b:

        a.append (elemento)

    b = b + [4]

    a[-1] = 100

    del b[0]

    return b[:]

if __name__ == "__main__":

    lista1= [1, 2, 3]

    lista2= [1, 2, 3]

    lista3= modifica (lista1, lista2)

    print (lista1)

'''

'''
lista = [9, 8, 3, 2, 0, 6, 7, 5, 1, 4]

LIMITE = len(lista)

i = 1

while i < LIMITE:

    j = 0

    while j < LIMITE -1:

        if lista[j] > lista[j+1]:

            temp = lista[j]

            lista[j] = lista[j+1]

            lista[j+1] = temp

        j = j + 1

    i = i + 1

print (lista)
'''
'''
nota1 = 2

nota2 = 3

nota3 = 3

promedio = nota1 + nota2 + nota3/3

if promedio >= 4.0:

      mensaje = "Alumno Aprobado"

else:

      mensaje = "Alumno Reprobado"

print (mensaje)

'''

'''
lista1 = [1, 2]

lista2 = [3, 4]

aux = lista1

lista1 = lista2

lista2 = aux

print (lista1, " - ", lista2)
'''

'''
def incrementa (a):

    a = a + 1 

    return a

if __name__ == "__main__":

    a = 1

    b = incrementa (a)

    print ("a: ", a, "- b: ", b)
'''

'''
i = 1

n = int(input())

while i < n:
    i = i - 1

print (i)

'''

'''
vocales = "aeiou"

linea = "esta es una linea de ejemplo para la prueba"

i = 0

cont = 0

while i < len(vocales):

     cont = cont + linea.count(vocales[i])

     i = i + 1

print (cont)

'''

'''

def minimo(var1, var2):

    if var1 < var2:

        return var1

    else:

        return var2

def suma(a, b):

    c = [ ]

    m = minimo(len(a), len(b))

    for i in range(m):

        c.append(a[i] + b[i])

    c = c + a[m:] + b[m:]

    return c

if __name__ == "__main__": 

    lista1 = [1, 6, 5, 4, 8]

    lista2 = [5, 2, 9]

    lista3 = suma(lista1, lista2)

    print (lista3)

'''

x = 3

      y = 7

      x = x - 1

      if x % 2 != 0:

            x = x + 1

      y = y - 1

      if y % 2 != 0:

            y = y + 1

      z = x + y

      print (x,'-',y,'-',z)