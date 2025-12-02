def mostrar_opciones():
    print("digita la letra a para actualizar sistema")
    print("digite la letra e para eleminar codigo")
    print ("digite la letra c para crear productos")
    print("digite la letra s para salir del programa")

def pedir_opcion():
    letra = input("digite su opcion")
    return letra

def buscar_respuesta(letra):
    if letra == "s":
        print("finalizo con exito")
    else :
        print("sigue dentro del while")
#codigo_principal():
while True:
    mostrar_opciones()
    letra = pedir_opcion()
    buscar_respuesta(letra)
    if letra == "s" :
     break
         
print("el do while ha finalizado")