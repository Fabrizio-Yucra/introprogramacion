import random

numero = int(input("Ingrese el tamaño de su Lista: "))
numv = int(input("Ingrese el numero del ultimo dijito: "))
contador = 1
v2 = []
v3 = []
while contador <= numero:
    v1 = random.randint(1, 300)
    a = str(v1)
    if a[-1] == str(numv):
        v3.append(v1)
    v2.append(v1)
    contador += 1
print("")
print(f"Su lista aleatoria de {numero} es: \n{v2}")
print("")
print(f"Numeros aleatorios de la lista terminados en {numv} son: \n{v3}")