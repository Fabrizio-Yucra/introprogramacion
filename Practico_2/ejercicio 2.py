def max_de_tres(numero_1, numero_2, numero_3):
    numero_mayor = 0
    if numero_1 > numero_mayor:
        numero_mayor = numero_1
    if numero_2 > numero_mayor:
        numero_mayor = numero_2
    if numero_3 > numero_mayor:
        numero_mayor = numero_3
    print(f"El numero Mayor es: {numero_mayor}")
num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese un numero: "))
num_3 = int(input("Ingrese un numero: "))

max_de_tres(num_1, num_2, num_3)
