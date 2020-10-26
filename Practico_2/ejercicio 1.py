def numeromayor(num_1, num_2):

    if num_1 > num_2:
        print(f"El numero mayor es: {num_1}")
    else:
        print(f"El numero mayor es: {num_2}")

numero_1 = float(input("Ingrese un numero: "))

numero_2 = float(input("Ingrese un segundo numero: "))

numeromayor(numero_1, numero_2)