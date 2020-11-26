num = str(input("Ingrese un numero: "))
tam = len(num)
mitad = tam // 2
contador = 0
contador1 = -1
contador2 = 0
while contador < mitad:
    if num[contador] == num[contador1]:
        contador += 1
        contador1 -= 1
        contador2 += 1
    else:
        contador += 1
        contador1 -= 1

if contador2 == mitad:
    print(f"El numero {num} es Capicua ")
else:
    print(f"El numero {num} no es Capicua")