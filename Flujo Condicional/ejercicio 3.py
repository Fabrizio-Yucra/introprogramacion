partido_1 = "MAS"
partido_2 = "Comunidad Ciudadana"
print(f"Los Partidos politicos son : {partido_1}, {partido_2}")
voto = str(input("ingrese un partido: "))
if voto == partido_1:
    print("Usted ha votado por: MAS" )
elif voto == partido_2:
    print("Usted ha votado por: Comunidad Ciudadana")
else:
    voto != partido_1 or voto != partido_2
    print("Voto invalido")