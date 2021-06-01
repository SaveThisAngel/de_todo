# while = ciclo
# try = exceptciones 
# len = return
# def = definicion
# format = devuelve una representación con formato del valor especificado controlado por el especificador de formato.
# sorted = devuelve una lista ordenada de los elementos en un iterable. 
# reverse =  devuelve el iterador invertido de la secuencia dada.
# join = devuelve una cadena uniendo todos los elementos de un iterable, separados por un separador de cadenas.
# \ =
# .format =
# .remove
# .pop
#


""" Valores Par e Inpar """

def obtenerNumero(texto):   # funcion para añadir un valor entero 
    # # # # # # # # # # while True:
        try:
            valor = int(input("{} : ".format(texto)))
            return valor
        except:
            print("El valor tiene que ser un numero")
 
valores=[]
texto=["Escribe el primer numero", "Escribe el segundo numero", "Escribe el tercer numero", "Escribe el cuarto numero", "Escribe el quinto numero"]
while len(valores)<5:
    valores.append(obtenerNumero(texto[len(valores)]))
 
# mostramos los valores ordenados ascendente
print("\n\nlos valores ordenados ascendente son: {}".format(sorted(valores)))
 
# mostramos los valores ordenados descendente
print("los valores ordenados descendente son: {}".format(sorted(valores, reverse=True)))
 
# mostramos los valores pares e impares
print("\n".join(["El valor {} es par".format(i) if i%2==0 else "El valor {} es impar".format(i) for i in valores]))