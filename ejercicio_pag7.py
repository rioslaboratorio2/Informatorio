
print("\nHola a continuacion ingrese los datos solicitados:\n")
preguntas = int(input("Ingrese la cantidad de Preguntas que respondio:\n"))
correctas = int(input("Ingrese el promedio Final de las respustas Correctas:\n"))


promedio = correctas/preguntas
resultado = promedio *100

if promedio > 90:
    print("El resultado es : EXCELENTE\t")

if promedio >= 70:
    print("El resultado es : BUENO\t")

if promedio >= 60:
    print("El resultado es : APROBADO0\t")

if promedio <60:
     print("El resultado es : NO ALCANZO\t")


print("Su Promedio final es : --->",resultado)
