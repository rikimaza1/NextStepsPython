# Crea un programa en Python donde la entrada sean una cadena de caracteres, una palabra y una palabra de reemplazo ,el resultado debe ser la cadena con todas las ocurrencias de la palabra reemplazadas por otra palabra.

# El programa debe utilizar un bucle while para buscar todas las ocurrencias de la palabra y reemplazarlas.

cadena= input("Introduce una cadena de caracteres")
palabra= input("Introduce la palabra a reemplazar")
palabraReemplazo= input("Introduce una palabra para remplazar")

# Con var = cadena.replace(palabra,palabraReemplazo se puede remplazar todas la concurrencias si usar un bucle while
while palabra in cadena:
    cadena = cadena.replace(palabra, palabraReemplazo)

print(cadena)