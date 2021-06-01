from random import random

i=1
cantIni=50
cantFin=250

print("CANT INI\tALEAT\tG/P\tCANT FIN")
while cantIni <=cantFin:
    aleatorio=random()
    if aleatorio<0.45:
        cantA=cantIni+1
        print("{}\t\t{}\tGANA\t{}".format(cantIni,str(aleatorio)[0:4],cantA))
    elif aleatorio<0.90:
        cantA=cantIni-1
        print("{}\t\t{}\tPIERDE\t{}".format(cantIni,str(aleatorio)[0:4],cantA))
    else:
        print("{}\t\t{}\t--\t{}".format(cantIni,str(aleatorio)[0:5],cantA))

    cantIni+=1
print("---------------------------------FIN-DEL-PROGRAMA-------------------------------")