numero = int(input("Ingrese un numero: "))
suma = 1
resultado = 0
f = f"*"
while suma <= numero:
    resultado = suma
    var_1 = suma - suma + 1
    print(var_1 * f)
    print(suma, end=" ")
    while resultado != 1:
        if resultado % 2 == 0:
            resultado = int(resultado / 2)
            var = resultado - resultado + 1
            print(var * f, end=" ")
        else:
            resultado = int((resultado * 3) + 1)
            var = resultado - resultado + 1
            print(var * f, end=" ")

    suma = suma + 1
print("*")