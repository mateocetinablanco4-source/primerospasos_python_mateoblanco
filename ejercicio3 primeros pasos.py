#zona de codigos python

def tomar_numero():

    numero = 1
    
    numero = int(input())
    return numero

def procesar_numero(numero):
        
        if numero % 2 == 0:
            print ("El número es par\n")

            return True
        else:
            print("El número es impar\n")
            
            return True

def impri_resultado():

    print("El programa finalizó.\n")



# codigo principal de python

numero = 1

while numero != 0:
        print("Digite un número: ")

        numero = tomar_numero() 

        if numero != 0:
             
             procesar_numero(numero)

impri_resultado()