def lectura_datos(nombre):
    ar = open(nombre)
    linea = ar.readline()
    linea = linea.rstrip('\n')    
    lis = linea.split(',')
    print(linea)
    print(lis[2]+' '+lis[3])
ar.close()
return lista

if __name__ == "__main__":
    datos = lectura_datos('titanic3.txt')
    print(datos)
