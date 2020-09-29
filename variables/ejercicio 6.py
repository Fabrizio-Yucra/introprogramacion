saludo = "buenos dias!"
nombre = input("¿comó te llamas? :")
peso = input("porfavor ingrese su peso en \"kg\"")
estatura = input("porfavor ingrese su estatura en \"m\"")
mensaje = "tu indice de masa corporal es"
imc = int(peso)/float(estatura)
print(saludo, nombre, mensaje, imc)