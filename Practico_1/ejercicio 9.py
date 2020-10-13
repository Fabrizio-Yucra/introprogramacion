operando = int(input("Operando: "))
operador = str(input("Operador: "))
operando_2 = int(input("Operando: "))
if operador == "+":
    resultado = operando + operando_2
    print(f"{operando} + {operando_2} = {resultado}")
if operador == "-":
    resultado = operando - operando_2
    print(f"{operando} - {operando_2} = {resultado}")
if operador == "*":
    resultado = operando * operando_2
    print(f"{operando} * {operando_2} = {resultado}")
if operador == "/":
    resultado = operando / operando_2
    print(f"{operando} / {operando_2} = {round(resultado, 3)}")
if operador == "**":
    resultado = operando ** operando_2
    print(f"{operando} ** {operando_2} = {resultado}")