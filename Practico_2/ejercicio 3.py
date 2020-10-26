def longitud_palabra(palabra):
    num = 0
    for a in palabra:
        num = num + 1
    print(num)
palabra_1 = input("Ingrese una palabra: ")
longitud_palabra(palabra_1)