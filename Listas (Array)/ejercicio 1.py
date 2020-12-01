num_I = int(input("Ingrese un número inicial: "))
num_F = int(input("Ingrese un número final: "))
l1 = []
lp = []
suma1 = 0
li = []
suma2 = 0
for a in range(num_I, num_F + 1):
    l1.append(a)
    if a % 2:
        lp.append(a)
        suma1 = suma1 + a
    else:
        li.append(a)
        suma2 = suma2 + a
print(l1)
print(f"Lista Par: {li}")
print(f"Suma: {suma2}")
print(f"Lista Impar: {lp}")
print(f"Suma: {suma1}")
