#Crea un programa que le pregunte al usuario su zona horaria y le muestre la hora actual en esa zona. 

#El programa debe manejar excepciones en caso de que la zona horaria ingresada no sea válida.
def ejercicio2():
   import pytz
   from datetime import datetime
   from pytz import timezone

   Ciudad = input("Por favor ingrese su ciudad: ")
   Continente = input("Por favor ingrese su continente: ")
   try:
      fecha = datetime.now(timezone(f"{Continente}/{Ciudad}"))
      print("La hora actual en ", Ciudad, "es:", fecha.strftime('%H:%M:%S'))

   except pytz.exceptions.UnknownTimeZoneError:
      print("La zona horaria ingresada no es válida")




