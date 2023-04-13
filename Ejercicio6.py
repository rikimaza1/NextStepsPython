#Crea un programa que le pida al usuario un número entero
#y luego calcule y muestre la suma de todos los números
#desde 1 hasta el número ingresado.

#El programa debe utilizar un bucle `for` para sumar los números.

def ejercicio6():
    try:
        numero = int(input("Introduca un número entero: "))
    except:
        print("El valor introducido no es un numero entero")

    else:
        suma = 0
        for i in range(1,numero+1,1):
            suma += i

        print("La suma total de los números es:", suma)