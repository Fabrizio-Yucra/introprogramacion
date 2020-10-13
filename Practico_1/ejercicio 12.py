numero = int(input("Cantidad de palabras: "))
suma = 0
num = 0
num1 = 1000
while suma < numero:
    suma = suma + 1
    palabra = input(f"Palabra {suma}: ")
    if len(palabra) > num:
        num = len(palabra)
        palabra_max = palabra
    if len(palabra) < num1:
        num1 = len(palabra)
        palabra_min = palabra
print(f"La palabra mas larga es {palabra_max}")
print(f"La palabra mas corta es {palabra_min}")
