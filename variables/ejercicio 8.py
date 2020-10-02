v1 = float(input("ingrese la capital inicial: "))
v2 = float(input("ingrese el interes anual: "))
v3 = float(input("ingrese el numero de años a invertir: "))
operacion_1 = v2 + int(1)
operacion_2 = float(operacion_1) ** v3
operacion_3 = float(operacion_2) * v1
print(f"El interés compuesto es {round(operacion_3, 2)}")