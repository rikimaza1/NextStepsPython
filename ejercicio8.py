# Crea un programa en Python que acepte una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que tienen más de 5 caracteres.

# El programa debe utilizar un bucle for para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.
def ejercicio8():
    lista = ["Manzana", "Pera", "Sandia", "Naranja", "Uva", "Fresa", "Mandarina"]
    print(f"La Lista es: {lista}")
    listaAux = []

    for x in lista:
        if len(x) > 5:
            listaAux.append(x)

    print(listaAux)
if __name__=="__main__":
    ejercicio8()        