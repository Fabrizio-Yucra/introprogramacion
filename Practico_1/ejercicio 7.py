numero = int(input("Ingrese un numero entero: "))
for a in range(1, numero +1):
    resto = numero % a
    if resto == 0:
        print(a)
