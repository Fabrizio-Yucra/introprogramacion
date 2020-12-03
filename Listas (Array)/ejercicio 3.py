base = int(input("Ingrese la base de su figura: "))
altura = int(input("Ingrese la altura de su figura: "))
numero = 1
lM = 0
lm = 0
if base > altura:
    lM = base
    lm = altura
else:
    lM = altura
    lm = base
no_entran = []
si_entran = []
while numero != 0:
    radio = int(input("Ingrese un radio: "))
    numero = radio
    if numero == 0:
        numero = 0
    diametro = 2 * radio
    if diametro <= lm:
        lm = lm - diametro
        lM = lM - diametro
        si_entran.append(radio)
    else:
        lm = lm
        no_entran.append(radio)
print(f"Los circulos que si pueden entrar a la figura son {si_entran}")
print(f"Los circulos que no pueden entrar a la figura son {no_entran}")