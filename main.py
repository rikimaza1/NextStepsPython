#Menú principal
import os
from ejercicio1 import ejercicio1
from ejercicio2 import ejercicio2
from ejercicio4 import ejercicio4
from ejercicio5 import ejercicio5
from ejercicio6 import ejercicio6
from ejercicio7 import ejercicio7
from ejercicio8 import ejercicio8
from ejercicio9 import ejercicio9
from ejercicio10 import ejercicio10
from ejercicio11 import ejercicio11

while True:
    os.system("cls") #Limpia la pantalla cada vez que se vuelve al menú
    print("Bienvenido/a al Menú principal. Este programa recoge todos los ejercicios de Algoritmos. Seleccione el algoritmo que desea usar de la lista.")
    print("1 - Cambio de formato de fecha")
    print("2 - Hora actual en zona horaria")
    print("3 - Contador de palabras de cadena")
    print("4 - Hora en formato de 24 horas")
    print("5 - Cadena invertida")
    print("6 - Suma de números hasta el introducido")
    print("7 - Imprimir cadena con saltos de linea")
    print("8 - Cadenas con más de 5 caracteres")
    print("9 - Reemplazar palabra en cadena")
    print("10 - Cadenas con vocales")
    print("11 - Lista de números múltiplos de 3")
 
    
    try:
        opcion = int(input("Introduzca el número del algoritmo que quiere usar o introduzca 0 para cerrar el programa: "))
    except Exception:
        print("No ha seleccionado un ejercicio válido")

    if opcion == 0: 
        input("Gracias por usar el programa. Pulse ENTER para salir.")
        break
    elif opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio2() 
    elif opcion == 4:
        ejercicio4()   
    elif opcion == 5:
        ejercicio5()  
    elif opcion == 6:
        ejercicio6()   
    elif opcion == 7:
        ejercicio7()  
    elif opcion == 8:
        ejercicio8()
    elif opcion == 9:
        ejercicio9() 
    elif opcion == 10:
        ejercicio10() 
    elif opcion == 11:
        ejercicio11()

    else:
        "No ha seleccionado un número correcto"
    input("Pulsa Enter para continuar.")    
    
    
    

    

