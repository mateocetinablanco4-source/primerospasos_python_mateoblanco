#zona de codigos paython


def tomar_numero():

    num = int(input("Digite el número: "))

    return num

def val_num(dato_numero):

    if dato_numero > 0:

        mensaje = "El número es positivo"
    elif dato_numero == 0:

        mensaje = "El número es neutro"
    else: 
        mensaje = "El número es negativo"

    return mensaje

def impri_dato(dato_mensaje):

    print("El número es: " + dato_mensaje)
           
# codigo principal de python


dato_numero = tomar_numero()

dato_mensaje = val_num(dato_numero)

impri_dato(dato_mensaje)  