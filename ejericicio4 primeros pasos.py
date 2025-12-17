#zona de codigos python

 
def pedir_cant():

    return int(input("digite la cantidad de números para sumar: "))

def acumular_suma(cant):

    sum = 0
    for i in range(cant):

        print("digite el número", i + 1, ": ", end="")

        numero = int(input())

        sum = sum + numero
    return sum


def ver_total(sum):

    print("la suma total es:", sum)



# codigo principal de python 


cant = pedir_cant() 

suma_total = acumular_suma(cant)

ver_total(suma_total)
