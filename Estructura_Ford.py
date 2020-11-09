from random import randrange


print("Bienvenidos, a continuacion digite los datos que le solicitaremos para las multiplicaciones :\n")

cantidad_multiplicaciones = int(input("Ingrese el numero de multiplicaciones que desea realizar:\n"))
cantidad_de_aciertos= 0

for j in range(0, cantidad_multiplicaciones):
    multiplicador = randrange(2,10)
    multiplicando= randrange(2,10)

    resultado_multiplicacion = multiplicador * multiplicando

    resultado = int(input("Ingrese por favor el resultado de {} x {} :\n".format(multiplicador,multiplicando)))
    desvio = (abs(resultado_multiplicacion - resultado)/resultado_multiplicacion)*100

    if desvio == 0:
        cantidad_de_aciertos += 1
    elif desvio <= 10:
        cantidad_de_aciertos += 0.66
    elif desvio > 10 and desvio <= 30:
        cantidad_de_aciertos += 0.33


nota = (cantidad_de_aciertos/cantidad_multiplicaciones)*100
print(f"La nota obtenida es:{nota}\t")

if nota >= 90:
        print("Felicitaciones por la nota obtenida\n")
