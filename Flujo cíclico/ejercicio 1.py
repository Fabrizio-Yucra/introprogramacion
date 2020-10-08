numero = int(input("Ingrese un numero positivo: "))
while numero < 0:
    print("Error, vuelva a ingresar un numero")
    numero = int(input("Ingrese un numero: "))
print("Ganaste")