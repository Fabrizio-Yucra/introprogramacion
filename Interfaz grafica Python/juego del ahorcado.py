def imprimirAhorcado(intentos):
    if intentos == 6:
        print("================")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if intentos == 5:
        print("================")
        print("=              |")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if intentos == 4:
        print("================")
        print("=              |")
        print("=              O")
        print("=")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if intentos == 3:
        print("================")
        print("=              |")
        print("=              O")
        print("=          ---------")
        print("=")
        print("=")
        print("=")
        print("=")
        print("===")
    if intentos == 2:
        print("================")
        print("=              |")
        print("=              O")
        print("=          ---------")
        print("=              |    ")
        print("=              |    ")
        print("=")
        print("=")
        print("===")
    if intentos == 1:
        print("================")
        print("=              |")
        print("=              O")
        print("=          ---------")
        print("=              |    ")
        print("=              |    ")
        print("=             /     ")
        print("=            /      ")
        print("===                 ")
    if intentos == 0:
        print("================")
        print("=              |")
        print("=              O")
        print("=          ---------")
        print("=              |    ")
        print("=              |    ")
        print("=             / \   ")
        print("=            /   \  ")
        print("===                 ")


txtpalabra = open("palabras_sencillas.txt", "r")
lista_de_palabras = txtpalabra.readlines()
txtpalabra.close()

wins = 0

while wins < 3:

    for palabraoculta in lista_de_palabras:
        palabraoculta = palabraoculta.strip()

        tam = len(palabraoculta)
        vectorPalabraOculta = []
        vectorPalabraGuiones = []
        intentos = 6

        for pos in range(0, tam, 1):
            vectorPalabraOculta.append(str(palabraoculta[pos]))
            vectorPalabraGuiones.append("-")

        print(vectorPalabraGuiones)

        while intentos > 0:

            print("Cantidad de intentos: ", intentos)
            coincidencias = 0
            cantidadguiones = 0
            letra = input("Ingrese una letra: ")

            for pos in range(0, tam, 1):
                if(letra.upper() == vectorPalabraOculta[pos]) or (letra.lower() == vectorPalabraOculta[pos]):
                    vectorPalabraGuiones[pos] = letra
                    coincidencias += 1

            print(vectorPalabraGuiones)

            for pos in range(0, tam, 1):
                if vectorPalabraGuiones[pos] == "-":
                    cantidadguiones = cantidadguiones + 1

            if coincidencias == 0:
                intentos -= 1
                imprimirAhorcado(intentos)
            else:
                intentos = intentos
                imprimirAhorcado(intentos)

            if cantidadguiones == 0:
                wins += 1
                if wins == 1:
                    print(f"Ganaste {wins} punto, adivinaste la palabra")
                else:
                    print(f"Ganaste {wins} puntos, adivinaste la palabra")

                intentos = -1

        if intentos == 0:
            print("Se terminaron tus intentos! Te ahorcaste!")
            wins = 100


txtpalabra = open("palabras_intermedias.txt", "r")
lista_de_palabras = txtpalabra.readlines()
txtpalabra.close()

while wins < 6:

    for palabraoculta in lista_de_palabras:
        palabraoculta = palabraoculta.strip()

        tam = len(palabraoculta)
        vectorPalabraOculta = []
        vectorPalabraGuiones = []
        intentos = 6

        for pos in range(0, tam, 1):
            vectorPalabraOculta.append(str(palabraoculta[pos]))
            vectorPalabraGuiones.append("-")

        print(vectorPalabraGuiones)

        while intentos > 0:

            print("Cantidad de intentos: ", intentos)
            coincidencias = 0
            cantidadguiones = 0
            letra = input("Ingrese una letra: ")

            for pos in range(0, tam, 1):
                if (letra.upper() == vectorPalabraOculta[pos]) or (letra.lower() == vectorPalabraOculta[pos]):
                    vectorPalabraGuiones[pos] = letra
                    coincidencias += 1

            print(vectorPalabraGuiones)

            for pos in range(0, tam, 1):
                if vectorPalabraGuiones[pos] == "-":
                    cantidadguiones = cantidadguiones + 1

            if coincidencias == 0:
                intentos -= 1
                imprimirAhorcado(intentos)
            else:
                intentos = intentos
                imprimirAhorcado(intentos)

            if cantidadguiones == 0:
                wins += 1
                if wins == 1:
                    print(f"Ganaste {wins} punto, adivinaste la palabra")
                else:
                    print(f"Ganaste {wins} puntos, adivinaste la palabra")

                intentos = -1

        if intentos == 0:
            print("Se terminaron tus intentos! Te ahorcaste!")
            wins = 100

txtpalabra = open("palabras_complejas.txt", "r")
lista_de_palabras = txtpalabra.readlines()
txtpalabra.close()

while wins < 9:

    for palabraoculta in lista_de_palabras:
        palabraoculta = palabraoculta.strip()

        tam = len(palabraoculta)
        vectorPalabraOculta = []
        vectorPalabraGuiones = []
        intentos = 6

        for pos in range(0, tam, 1):
            vectorPalabraOculta.append(str(palabraoculta[pos]))
            vectorPalabraGuiones.append("-")

        print(vectorPalabraGuiones)

        while intentos > 0:

            print("Cantidad de intentos: ", intentos)
            coincidencias = 0
            cantidadguiones = 0
            letra = input("Ingrese una letra: ")

            for pos in range(0, tam, 1):
                if (letra.upper() == vectorPalabraOculta[pos]) or (letra.lower() == vectorPalabraOculta[pos]):
                    vectorPalabraGuiones[pos] = letra
                    coincidencias += 1

            print(vectorPalabraGuiones)

            for pos in range(0, tam, 1):
                if vectorPalabraGuiones[pos] == "-":
                    cantidadguiones = cantidadguiones + 1

            if coincidencias == 0:
                intentos -= 1
                imprimirAhorcado(intentos)
            else:
                intentos = intentos
                imprimirAhorcado(intentos)

            if cantidadguiones == 0:
                wins += 1
                if wins == 1:
                    print(f"Ganaste {wins} punto, adivinaste la palabra")
                else:
                    print(f"Ganaste {wins} puntos, adivinaste la palabra")

                intentos = -1

        if intentos == 0:
            print("Se terminaron tus intentos! Te ahorcaste!")
            wins = 100
