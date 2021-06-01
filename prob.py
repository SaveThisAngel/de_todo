import random

def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint(0, 1000)
      return lista

n=int(input("maximo de numeros: "))

lista=listaAleatorios(n)
print(lista,'\n')


def ordburbuja(lista):
    for dato in range(len(lista)-1,0,-1):
        for i in range(dato):
            if lista[i]>lista[i+1]:
                ter = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = ter



#lista = [123,1,86,1002,43,21,37,57,666786]
ordburbuja(lista)
print('La nueva lista es: \n',  lista)	