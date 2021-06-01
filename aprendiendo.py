#calculador

"""

def calcular():
    operacion = input('''
Ingresa un signo para proceder a calcular:
+ para suma
- para resta
* para multiplicacion
/ para division
# # # # # # # # ''')
 
    
    numero1 = int(input('Introducir el primer numero: '))
    numero2 = int(input('Introducir el segundo numero: '))
    if operacion == '+':
        print(numero1 + numero2)

    elif operacion == '-':
        print(numero1 - numero2)

    elif operacion == '*':
        print(numero1 * numero2)

    elif operacion == '/':
        print(numero1 / numero2)     

calcular()                


"""

#1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

"""
def max(a,b):
    if a > b:
        print("a es mayor")
        return a
    elif b > a:
        print("b es mayor")
        return b    

max(2,5)

"""

