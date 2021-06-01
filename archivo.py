#Autor: Benjamin Charnock Verdugo
#Fecha: 23 de junio 2020
#Descripcion: desgloso de presupuesto de un hospital.

#ginecologia 40%
#traumatologia 30%
#pediatria 30%

if __name__ == "__main__":
    presupuesto = int(input("indique el presupuesto de el hospital: "))
    ginecologia = presupuesto * 0.4
    traumatologia = presupuesto * 0.3
    pediatria = presupuesto * 0.3
    print("A ginecologia le corresponde: ", ginecologia)
    print("A traumatologia le corresponde: ", traumatologia)
    print("A pediatria le corresponde: ", pediatria)

