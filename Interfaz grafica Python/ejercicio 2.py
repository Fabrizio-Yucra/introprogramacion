v1 = []
contador = 1

while contador <= 5:
    num = int(input("Ingrese un numero para el vector 1: "))
    v1.append(num)
    contador += 1
print("")
v2 = []
contador2 = 1
while contador2 <= 5:
    num2 = int(input("Ingrese un numero para el vector 2: "))
    v2.append(num2)
    contador2 += 1
print("")
vr = []
contador3 = 0
while contador3 <= 4:
    resultado = int(v1[contador3]) + int(v2[contador3])
    vr.append(resultado)
    contador3 += 1

print(f"El vector 1 es: {v1}")
print(f"El vector 2 es: {v2}")
print(f"La suma de los vectores es {vr}")