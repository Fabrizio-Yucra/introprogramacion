def inversa(palabra):
    tamaño_palabra = len(palabra)
    while tamaño_palabra != 0:
        tamaño_palabra -= 1
        print(palabra[tamaño_palabra], end="")
palabra_1 = str(input("Ingrese una palbra: "))
inversa(palabra_1)