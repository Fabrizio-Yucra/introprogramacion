año = int(input("Ingrese un año: "))
operacion = año % 4
operacion_1 = año % 400
operacion_2 = año % 100
if operacion == 0:
    print("El año es bisiesto")
elif operacion_1 == 0:
    print("El año es bisiesto")
elif operacion_2 == 0:
    print("El año no es bisiesto")
else:
    print("El año no es bisiesto")