def factorial(a):
    num = a
    FACT = []
    contador = 1
    while contador <= 20:
        numero = str(contador) + "!"
        FACT.append(numero)
        contador += 1
    print(FACT)

    multi = 1
    while a > 1:
        multi = a * multi
        a -= 1
    print(f"El factorial de {num} es: {multi}")

factorial(5)