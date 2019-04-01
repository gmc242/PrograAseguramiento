
def main():

    #print(fecha_es_tupla((2015,4,2)))
    #print(bisiesto(2020))
    #print(fecha_es_valida((2020,2,30)))
    #print(dia_siguiente((2020, 2, 29)))
    print(dias_desde_primero_enero((2019, 4, 1)))

# R0 se encarga de verificar si es una tupla de 3 valores positivos enteros
# Input esperado: Un tipo de datos Tupla (tuple) con un largo de 3 (len(fecha) == 3)
# Tipo de retorno: Booleano
# Retorno: True si es una tupla de 3 enteros positivos, False de otro modo
# Requerimiento R0
def fecha_es_tupla(fecha):

    # Revisa el tipo y largo de la tupla como filtro inicial
    if(type(fecha) == tuple and len(fecha) == 3):
        
        # Se intentará obtener un entero por cada valor en la fecha por lo que es necesario el try-catch
        try:
            
            #Tomamos cada elemento de la fecha(año,mes,dia) y vemos si es positivo
            for item in fecha:
                if(int(item) < 0):                              
                    print("Deben ser numeros positvos")
                    return False # Algún valor es menor a 0
            
            # Se revisaron todos los casos necesarios y los aprobó todos la fecha, es tupla correctamente
            return True

        # Si existe un Exception es debido a que el cast falló por lo que los valores en la tupla no son enteros
        except Exception:
            return False

    # No cumple con el primer filtro básico
    else:
        return False

#R0((2015,4,2))

# Esta función se encarga de hacer un pequeño cálcula para revisar si uno año es bisiesto o no
# Input esperado: Un entero positivo, correspondiente a un año
# Tipo de retorno: Booleano
# Retorno: True si el año es bisiesto, False de otro modo.
# Requerimiento R1
def bisiesto(anio):

    # p = (año divisible por 4)
    # q = (año divisible por 100)
    # r = (año divisible por 400)

    # año es bisiesto si y solo si p and ((not q) or r)
    # Fuente del algoritmo: https://es.wikipedia.org/wiki/A%C3%B1o_bisiesto

    # Primero revisa si el año es válido.
    # Bajo cualquier flujo normal, se esperaría que el chequeo se haya hecho antes.
    # Aún así, por robustez y seguridad se hace la revisión de nuevo.
    if isinstance(anio, int) and (anio > 0):
        return (anio % 4 == 0) and ((anio % 100 != 0) or (anio % 400 == 0))
    else:
        return False

#R1(2304)

# Esta función se encarga de retornar el mayor día posible para un mes dado
# Input: Dos enteros correspondientes al mes y año (para ver si es bisiesto o no)
# Tipo de Retorno: Entero
# Retorno:  [28,29] si el mes es Feb
#           [30] si el mes es Abr, Jun, Sep o Nov
#           [31] si el mes es Ene, Mar, May, Jul, Ago, Oct o Dic 
# Auxiliar para requerimiento R2, R3
def maximo_dia_por_mes(mes, anio):

    # La cantidad de días por mes continúa un patrón fácil de observar,
    # la cantidad alterna entre 31 y 30 (28 o 29 para Febrero) según la paridad del número de mes
    # El ciclo se reinicia en Agosto
    # ((mes % 7) % 2) Indica la paridad mencionada, si es 0 la cantidad de días será 30.
 
    # Febrero es un caso especial, se debe revisar si es bisiesto.
    if mes == 2:
        if(bisiesto(anio)):
            return 29 # Es bisiesto
        else: 
            return 28 # No es bisiesto

    # Revisa la lógica mencionada anteriormente de la paridad por mes.
    elif ((mes % 7) % 2) == 0:
        return 30 # Es par
    else:
        return 31 # Es impar

# Esta función se encarga de realizar una validación sobre los datos ingresados
# Input esperado: Una tupla con el formato válido de fecha
# Tipo de retorno: Booleano
# Retorno: True si es una fecha coherente con el calendario Gregoriano, False de otro modo
def fecha_es_valida(fecha):

    if not fecha_es_tupla(fecha):
        print("La fecha no es una tupla válida. Por favor ingrese una fecha en el formato válido.")
        return False
    else:
        
        anio = fecha[0]
        mes = fecha[1]
        dia = fecha[2] # Estas asignaciones permiten mayor claridad en el código posterior

        # Revisa el rango del mes
        if mes > 0 and mes < 13:
            # Revisa el rango del dia con la función auxiliar programada
            if dia > 0 and (dia <= maximo_dia_por_mes(mes, anio)):
                return True # El día está en un rango válido para el mes y año ingresado
            else:
                return False # El día no está en un rango válido para el mes y año ingresado
        else:
            return False # El mes no está en el rango válido [1, 12]

#print(fecha_es_valida((2020,2,30)))

# Esta función se encarga de retornar para cualquier fecha su día siguiente en el formato establecio
# Input esperado: Una tupla (tuple) de tres valores enteros que represente una fecha válida
# Tipo de retorno: Una tupla de tres valores enteros, que representa una fecha válida
# Retorno: La fecha correspondiente al próxima día de la fecha ingresada.
def dia_siguiente(fecha):

    if fecha_es_valida(fecha):
        anio = fecha[0]
        mes = fecha[1]
        dia = fecha[2] # Estas asignaciones permiten mayor claridad en el código posterior

        # Si el día más uno es menor al rango de un mes dado es el caso más simple
        if (dia+1) <= maximo_dia_por_mes(mes, anio):
            return (anio, mes, dia+1) # Se retorna la fecha, más un día
        else:
            # Si el día es mayor al rango del mes, se revisa si el próximo mes está en el rango válido
            if (mes+1) <= 12:
                return (anio, mes+1, 1) # Se retorna la fecha como el primero del siguiente mes
            else:
                # Se debe cambiar de año
                return (anio+1, 1, 1) # Se retorna el primero de enero del año siguiente

    else:
        raise Exception("La fecha ingresada no es válida.")

# Esta función se encarga de calcular los dias transcurridos hasta una fecha indicada,
# desde el primero de enero del mismo año de la fecha.
# Input esperado: Una tupla (tuple) correspondiente a una fecha válida
# Tipo de retorno: Un entero (int)
# Retorno: Cantidad de días transcurridos desde el primero de enero de un año hasta una fecha dada en ese año.
# Tomando en cuenta que la especificación del requerimiento exige que:
# El transcuro entre el primero de enero y el mismo día es 0.
def dias_desde_primero_enero(fecha):

    if fecha_es_valida(fecha):

        anio = fecha[0]
        mes = fecha[1]
        dia = fecha[2] # Estas asignaciones permiten mayor claridad en el código posterior

        # Se cuentan los dias del mes actual
        dias_transcurridos = dia

        # Por cada mes se agregan los días transcurridos
        for mes_i in range(1, mes):
            dias_transcurridos += maximo_dia_por_mes(mes_i, anio)

        return dias_transcurridos - 1 # Por definición desde el primero de enero al mismo dia deben haber 0 días

    else:
        raise Exception("La fecha ingresada no es válida.")
    

# Convención de Python para ejecutar el método main
if __name__ == "__main__":
    main()
