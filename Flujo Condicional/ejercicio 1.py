n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un segundo número: "))
n3 = int(input("Ingrese un tercer número: "))
operacion_1 = n1 * int(100)
operacion_2 = n2 * int(10)
operacion_3 = operacion_2 + operacion_1 + n3
if operacion_3 == int(777):
    print("Ganaste!")
