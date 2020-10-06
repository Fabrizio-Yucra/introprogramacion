monto = float(input("Ingrese el consumo de agua en m3: "))
mensaje = "Tu monto a pagar es de: "
if monto <= 100:
    print(mensaje, monto * 1.00, "Bs")
elif 100 < monto <= 499:
    print(mensaje, monto * 1.20, "Bs")
elif 500 <= monto <= 999:
    print(mensaje, monto * 1.50, "Bs")
elif monto >= 1000:
    print(mensaje, monto * 2.00, "Bs")


