#Crea un programa en Python que acepte una cadena de
#caracteres y devuelva la cadena invertida
#(por ejemplo, "hola" se convertiría en "aloh"). 

#El programa debe utilizar un bucle `for`
#para recorrer la cadena y construir la cadena invertida.
def ejercicio5():
    try:
        cadena = input("Introduzca una frase: ")

    except:
        print("El valor introducido no e suna frase")
    
    else:
        cadenaInvertida = ""

        for i in range(len(cadena)-1,-1,-1):
            cadenaInvertida += cadena [i]

        print ("La cadena invertida es:", cadenaInvertida)
if __name__=="__main__":
    ejercicio5()