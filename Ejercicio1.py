#1. Crea un programa en Python que acepte una fecha como cadena de caracteres en formato `"dd/mm/aaaa"` y devuelva la fecha en formato `"aaaa-mm-dd"`, con el año primero. 

 #  El programa debe manejar excepciones en caso de que la cadena no tenga el formato correcto.
def ejercicio1():
    from datetime import datetime

    while True:
        fechaCadena = input("Introduzca una fecha en formato dd/mm/aaaa: ")

        try: 
            fecha = datetime.strptime(fechaCadena, "%d/%m/%Y")
            fechaNueva = fecha.strftime("%Y-%m-%d")
            print(f"Nueva fecha: {fechaNueva}")
            break

        except:
            print("Error en el formato")
