variable_1 = input("Ingrese una palabra: ")
variable_2 = input("ingrese otra palabra: ")
if len(variable_1) > len(variable_2):
    print(f"La palabra {variable_1} tiene {len(variable_1) - len(variable_2)} letras mas que {variable_2}")
elif len(variable_1) == len(variable_2):
    print("Las dos palabras tienen el mismo largo")
else:
    print(f"La palabra {variable_2} tiene {len(variable_2) - len(variable_1)} letras mas que {variable_1}")
