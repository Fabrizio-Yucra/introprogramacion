numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese un segundo numero: "))
numero_3 = int(input("Ingrese un tercer numero: "))
if numero_3 > numero_2 and numero_3 > numero_1:
    if numero_2 > numero_1:
        print(numero_1, numero_2, numero_3)
if numero_2 > numero_1 and numero_2 > numero_3:
    if numero_1 > numero_3:
        print(numero_3, numero_1, numero_2)
if numero_1 > numero_2 and numero_1 > numero_3:
    if numero_2 > numero_3:
        print(numero_3, numero_2, numero_1)
if numero_3 > numero_2 and numero_3 > numero_1:
    if numero_1 > numero_2:
        print(numero_2, numero_1, numero_3)
if numero_2 > numero_1 and numero_2 > numero_3:
    if numero_3 > numero_1:
        print(numero_1, numero_3, numero_2)
if numero_1 > numero_2 and numero_1 > numero_3:
    if numero_3 > numero_2:
        print(numero_2, numero_3, numero_1)



