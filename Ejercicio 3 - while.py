def pedir_numero():
    print("digite el numero")
    num = int(input())
    return num
def prosesar_numero(num):
    if num % 2 == 0 :
        mensaje = ("el numero es par")
        return mensaje
    else:
        mensaje=("el numero es impar")
        return mensaje 
def mostrar_mensaje(mensaje):
    print(mensaje)

#principa_codigo
num= pedir_numero()
mensaje = prosesar_numero(num)
mostrar_mensaje(mensaje)
    

