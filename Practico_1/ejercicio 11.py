from datetime import date

print("Ingrese su fecha de nacimiento.")
dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

fecha_de_nacimiento = date(año, mes, dia)
hoy = date.today()
operacion = (hoy.year - fecha_de_nacimiento.year)
operacion_1 = (hoy.day - fecha_de_nacimiento.day)
operacion_2 = (hoy.month - fecha_de_nacimiento.month)
if operacion_2 <= 0:
    if operacion_1 >= 0:
        print(f"Usted tiene {operacion} años. ")
    else:
        print(f"Usted tiene {operacion -1} años. ")
else:
    print(f"Usted tiene {operacion} años. ")

