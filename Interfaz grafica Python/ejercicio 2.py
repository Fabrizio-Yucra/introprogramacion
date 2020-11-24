v1 = []
contador = 1
suma = 0
while contador <= 5:
    num = int(input("Ingrese un numero para el vector 1: "))
    v1.append(num)
    contador += 1
    suma = suma + num
suma2 = 0
v2 = []
contador2 = 1
while contador2 <= 5:
    num2 = int(input("Ingrese un numero para el vector 2: "))
    v2.append(num2)
    contador2 += 1
    suma2 = suma2 + num2

operacion = suma + suma2
print(f"La suma de los vectores es {operacion}")