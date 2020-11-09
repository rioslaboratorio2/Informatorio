# primera forma de resolver el problema

#print("\n")
#for i in range (100, 1000):
#    centena= i // 100
#    decena = (i//10) % 10
#    unidad = i % 10

#   if (centena**3 + decena**3 + unidad **3) == i:
#       print("Este numero cumple la condicion\t--->:",i)

# segunda forma de resolver el problema usando unos metodos de python

for i in range (100, 1000):
    s = str(i)
    suma = 0

    for x in s:
        suma = suma + int(x)**3
        if suma == i:
            print("Este numero cumple la condicion\t--->:", i)
