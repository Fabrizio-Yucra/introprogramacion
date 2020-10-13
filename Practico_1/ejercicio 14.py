nombre = input("Cual es tu nombre: ")
estatura = float(input("Ingrese su estatura en m: "))
peso = float(input("Ingrese su peso kg: "))
edad = float(input("Ingrese su edad: "))
IMC = float(peso / estatura ** 2)
if edad < 45:
    if IMC < 22.0:
        print(f"Hola! {nombre} tu riesgo de padecer enfermedades coronarias es baja. Sigue en ese estado de salud")
    elif IMC >= 22.0:
        print(f"Hola! {nombre} tu riesgo de padecer enfermedades coronarias es medio. Intenta mejorar tu estado de salud")
elif edad >= 45:
    if IMC < 22.0:
        print(f"Hola! {nombre} tu riesgo de padecer enfermedades coronarias es medio. Intenta mejorar tu estado de salud")
    elif IMC >= 22.0:
        print(f"Hola! {nombre} tu riesgo de padecer enfermedades coronarias es alto. Mejore su estado de salud")

