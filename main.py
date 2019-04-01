
def main():

    print("Hola")

#R0 se encarga de verificar si es una tupla de 3
def R0(fecha):

    partes= fecha.split(",")                            #Separamos la fecha por comas, haciendo un esplit
    if len(partes) != 3:                                #Si el split es diferente de 3 no es una fecha completa o pusieron mas datos
        print("No es tupla")
        return False


    for item in partes:
        if(int(item) < 0):                              #Tomamos cada elemento de la fecha(año,mes,dia) y vemos si es positivo
            print("Deben ser numeros positvos")
            return False
    print("Si es tupla")
    return True

#R0("2015,2,4")
def R1(bisiesto):                                       #https://es.wikihow.com/calcular-los-a%C3%B1os-bisiestos

    if( bisiesto % 4 == 0):                             #Se Tiene que ver si es divisible entre 4, si lo es sigue a otra prueba, sino no lo es

        if(bisiesto % 100 != 0):                        #Se revisa si es divisible entre 100, si si es divisible, se hace otra prueba, sino ya demuestra ser bisiesto
            return True

            if(bisiesto % 400 == 0):                    #La ultima prueba es probar si es divisible entre 400, si lo es, es bisiesto
                return True
    else:
        return False

#R1(2304)



