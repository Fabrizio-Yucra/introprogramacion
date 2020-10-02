from datetime import date

dia = int(input("introduzca el dia de nacimiento: "))

mes = int(input("introduzca el mes de nacimiento: "))

año = int(input("introduzca el año de nacimiento: "))

fecha_de_nacimiento = date(año, mes, dia)

hoy = date.today()
operacion = int(hoy.year - fecha_de_nacimiento.year)
if operacion > 18:
    print("El usuario es mayor 18 años")
else:
    print("El usuario es menor a los 18 años")
