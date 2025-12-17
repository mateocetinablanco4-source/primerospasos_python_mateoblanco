
# zona de funciones python

def tomar_letra():
    letra = str(input())
    return letra

def continuacion(letra):
    if letra == 'S' or letra == 's':
        print("Finalizó con exito. \n")
        return False
    else:
        print("Sigue dentro del proceso del DO-WHILE \n")
        return True

def imprimir_mensaje_final():
    print("El proceso DO-WHILE ha finalizado. \n")


# codigo principal de python

while True:  
    print("digite la letra 'A' para Actualizar Sistema")
    print("digite la letra 'E' para Eliminar Catalogo")
    print("digite la letra 'C' para Crear Productos")
    print("digite la letra 'S' para salir del programa")

    letra = tomar_letra()      
    continua = continuacion(letra)

    if not continua:
        break

imprimir_mensaje_final()


