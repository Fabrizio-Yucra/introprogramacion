def letra(letra_1):
    if letra_1 == "a" or letra_1 == "e" or letra_1 == "i" or letra_1 == "o" or letra_1 == "u":
        print(True)
    else:
        print(False)
caracter = str(input("Introduce un caracter: "))
letra(caracter)