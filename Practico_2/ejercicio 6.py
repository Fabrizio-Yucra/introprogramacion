def es_palindromo(palabra):
    div = len(palabra) // 2
    rest = len(palabra) - 1
    contador = 0
    contador_1 = 1

    while contador != div:
        if str(palabra[contador]) == str(palabra[rest]):
            contador_1 = contador + 1

        contador = contador + 1
        rest = rest - 1

    if contador_1 * 2 == len(palabra) or (contador * 2) + 1 == len(palabra):
        print(True)
    else:
        print(False)


pal = str(input("Ingrese una palabra: "))

es_palindromo(pal)