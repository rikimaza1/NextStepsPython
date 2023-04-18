#Crea un programa en Python que tome una cadena de caracteres y devuelva el número de palabras que contiene. 

#El programa debe utilizar un bucle `while` para recorrer la cadena y contar las palabras.

def ejercicio3():
    try:
        frase = input("Introduzca una palabra o frase: ")

    except:
        print("El valor introducido no es una palabra o frase")

    else:
        i=0
        contador=0
        while(i<len(frase)):
            if(frase[i]== ' '):
                contador+=1
                
                while (i < len(frase) and frase[i] == ' '):
                        i += 1
            else:
                i += 1

        contador += 1
        print(f"El numero de palabras es {contador}" )
if __name__=="__main__":
    ejercicio3()

