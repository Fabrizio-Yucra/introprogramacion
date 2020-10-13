valor = int(input("Ingrese un valor: "))
suma = 0

for termino in range(1, valor + 1):
    if termino % 2 == 0:
        i = -1
    else:
        i = 1
    operacion = i / (1 + 2 *(termino - 1))
    suma = suma + operacion
valor_pi = 4 * suma
print(valor_pi)