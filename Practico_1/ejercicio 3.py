numero_1 = int(input("Ingrese un numero entero: "))
numero_2 = int(input("ingrese un segundo numero entero: "))
if numero_1 % numero_2 == 0:
    print(f"La division es exacta")
    print(f"Cociente = {numero_1 / numero_2} ")
    print(f"Resto = 0")
else:
    print(f"La division no es exacta")
    print(f"Cociente = {numero_1 // numero_2}")
    print(f"Resto = {numero_1 % numero_2}")
