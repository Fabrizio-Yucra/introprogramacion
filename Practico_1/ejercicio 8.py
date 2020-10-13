numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese un segundo numero: "))

def sumalista(listaNumeros):
    numero = 0
    for i in range(numero_1 + 1, numero_2):
        numero = numero + i
    return numero
print(sumalista([]))