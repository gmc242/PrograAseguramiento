
def main():

    print("Hola")

#R0 se encarga de verificar si es una tupla de 3
def R0(fecha):

    if(type(fecha) == tuple and len(fecha) == 3):
        return True
    return False


#R0((2015,4,2))


def R1(bisiesto):                                       #https://es.wikihow.com/calcular-los-a%C3%B1os-bisiestos

    return (bisiesto % 4 == 0) and ((bisiesto % 100 != 0) or (bisiesto % 400 == 0))

#R1(2304)


def R2(fecha):
    if len(fecha) != 3:                                #Si el split es diferente de 3 no es una fecha completa o pusieron mas datos
        print("No es tupla de 3")
        return False


    for item in fecha:
        if(int(item) < 0):                              #Tomamos cada elemento de la fecha(año,mes,dia) y vemos si es positivo
            print("Deben ser numeros positvos")
            return False
    return True

#print(R2((2015,5,5)))
