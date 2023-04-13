# Crea un un programa en Python que tome una lista de cadenas de caracteres y devuelva una nueva lista que contenga solo las cadenas que contienen al menos una vocal.

# La función debe utilizar un bucle for para recorrer la lista y una estructura de control de flujo para filtrar las cadenas.

lista = ["ZZz", "Pera", "Shhhh!", "Naranja", "Pff", "Fresa", "Mandarina"]
listaAux = []

for x in lista:
    if "a" in x or "e" in x or "i" in x or "o" in x or "u" in x :
        listaAux.append(x)

print(listaAux)        