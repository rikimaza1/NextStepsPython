# Crea un programa en Python que tome una lista de números enteros y devuelva una nueva lista que contenga solo los números que son múltiplos de 3.

# El programa debe utilizar un bucle for para recorrer la lista y una estructura de control de flujo para filtrar los números.
def ejercicio11():
    listaEnteros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"La lista es: {listaEnteros}")
    numero = 3
    listaAux = []

    for x in listaEnteros:
        if x % numero == 0:
            listaAux.append(x)

    print(listaAux)