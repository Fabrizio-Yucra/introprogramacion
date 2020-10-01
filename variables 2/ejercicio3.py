import math

radio = float(input("ingrese el radio :"))
area = math.pi * radio**2
perimetro = 2 * math.pi * radio
mensaje = f"El área de la circunferencia {area}. El perimetro de la circunferencia es {perimetro}"
print(mensaje)

