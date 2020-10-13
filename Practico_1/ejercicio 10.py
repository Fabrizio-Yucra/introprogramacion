tiempo = int(input("Duracion de tramo: "))
suma = 0
while tiempo > 0:
    suma = tiempo + suma
    tiempo = int(input("Duracion de tramo: "))
operacion = suma // 60
operacion_1 = suma % 60
if operacion_1 < 10:
    print(f"Tiempo total de viaje: {operacion}:0{operacion_1} horas")
else:
    print(f"Tiempo total de viaje: {operacion}:{operacion_1} horas")