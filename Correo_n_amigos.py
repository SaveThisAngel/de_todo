"""
correo = str(input("Ingrese su correo: "))

valido = True

x = correo.find("@")

if x == -1:
    valido = False

print(valido)
"""
"""

#Numeros amigos (shecho)

def divisores (num):
    vec = []
    for i in range(1, num):
        if num%i == 0:
            vec.append(i)
    return vec

def sumatoria (vec):
    sumatoria = 0
    for k in vec:
        sumatoria = sumatoria + k
    return sumatoria

numero_a = int(input("Introduzca el primer numero: "))
numero_b = int(input("Introduzca el segundo numero: "))                 

num_a = int(numero_a)
num_b = int(numero_b)

vec_a = divisores(num_a)
vec_b = divisores(num_b)

sum_a = sumatoria(vec_a)
sum_b = sumatoria(vec_b)

if sum_a == num_b and sum_b == num_a:
    print("son numeros amigos")
else:
    print("no son numeros amigos")    
"""