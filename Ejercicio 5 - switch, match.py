
# zona de funciones


def tomar_numero():
    return int(input("Digite un numero del 1 al 12: "))

def procesar_resultado(num):
    match num:
        case 1:
            print ("El mes es Enero.")
        case 2:
            print ("El mes es Febrero.")
        case 3:
            print ("El mes es Marzo.") 
        case 4:
            print ("El mes es Abril.")
        case 5:
            print ("El mes es Mayo.")
        case 6:
            print ("El mes es Junio.")
        case 7:
            print ("El mes es Julio.")
        case 8:
            print ("El mes es Agosto")
        case 9:
            print("El mes es Septiembre") 
        case 10:
            print("El mes es Octubre.")
        case 11:
            print ("El mes es Noviembre.")
        case 12:
            print ("El mes es Diciembre.")

def imprimir_resultado():
    print("El programa finalizó. ")

# CÓDIGO PRINCIPAL. 

num = tomar_numero() 

procesar_resultado(num)

imprimir_resultado()