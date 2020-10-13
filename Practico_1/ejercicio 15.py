numero = int(input("Ingrese un numero: "))
print(int(numero), end=" ")
while numero != 1:
    if numero % 2 == 0:
        numero = numero / 2
        print(int(numero), end=" ")

    else:
        numero = (numero * 3) + 1
        print(int(numero), end=" ")




