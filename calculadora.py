def calcular():
    operacion = input('''
Porfavor elige la operacion que deseas realizar:
+ para suma
- para resta
* para multiplicacion
/ para divicion
''') 
 
    numero_1 = int(input('Introduce el primer numero: '))
    numero_2 = int(input('Introduce el segundo numero: '))
 
    if operacion == '+':
        print('{} + {} ='.format(numero_1, numero_2), end=" ")
        print(numero_1 + numero_2)
 
    elif operacion == '-':
        print('{} - {} ='.format(numero_1, numero_2), end=" ")
        print(numero_1 - numero_2)
 
    elif operacion == '*':
        print('{} * {} ='.format(numero_1, numero_2), end=" ")
        print(numero_1 * numero_2)
 
    elif operacion == '/':
        print('{} / {} ='.format(numero_1, numero_2), end=" ")
        print(numero_1 / numero_2)
 
    else:
        print('No se a escrito un operador valida, ejecute el programa de nuevo.')
 
    again()
 
def again():
    calcular_denuevo = input('''
Quieres Calcular denuevo?
Porfavor escribe S para SI o N para NO.
''')
 
    if calcular_denuevo.upper() == 'S':
        calcular()
    elif calcular_denuevo.upper() == 'N':
        print("Chau.")
    else:
        again()
 
calcular()
