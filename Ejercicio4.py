import datetime

def ejercicio4():
    while True:
        user_input = input("Ingrese una hora en formato hh:mm AM/PM: ")
        try:
            hora, minutos_ampm = user_input.split(":")
            minutos, am_pm = minutos_ampm.split()
            hora = int(hora)
            minutos = int(minutos)
            if am_pm not in ['AM', 'PM']:
                raise ValueError
            if hora <1 or hora >12 or minutos <0 or minutos > 59:
                print("Hora ingresada no válida. Intentelo de nuevo")
                continue

            if am_pm == 'PM' and hora != 12:
                hora += 12
            elif am_pm == 'AM' and hora == 12 :
                hora = 0

            time_obj = datetime.datetime(1,1,1,hora,minutos)
            time_str = time_obj.strftime("%H:%M")
            print("La hora en formato de 24 horas es: ", time_str)
            break
        except ValueError:
            print("Formato de hora incorrecto. Intentelo de nuevo")
            continue
if __name__=="__main__":
    ejercicio4()

    