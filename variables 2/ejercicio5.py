numero_1 = float(input("ingrese un numero: "))
operacion_1 = numero_1 == int(5)
print(f"El número es igual a 5: {operacion_1}")
operacion_2 = numero_1 == 5.0
print(f"El número es igual que 5.0: {operacion_2}")
operacion_3 = int(10) > numero_1 > int(0)
print(f"El número es mayor que 0 y menor que 10: {operacion_3}")
operacion_4 = numero_1 < int(0)
operacion_5 = numero_1 > int(10)
if operacion_4 or operacion_5:
    print("El número es menor que 0 o mayor que 10: True")
else:
    print("El número es menor que 0 o mayor que 10: False")
operacion_6 = numero_1 == 5
operacion_7 = int(20) > numero_1 > int(10)
if operacion_6 or operacion_7:
    print("El número es igual a 5, o en caso de no serlo, si es mayor que 10 y menor que 20: True")
else:
    print("El número es igual a 5, o en caso de no serlo, si es mayor que 10 y menor que 20: False")


