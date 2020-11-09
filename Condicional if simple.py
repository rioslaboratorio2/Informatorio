
print("Bienvenidos")

precio = float(input("Ingrese el precio por unidad:"))
unidad = int(input("Ingrese la cantidad a llevar:"))

if unidad >= 10:
    total = unidad * precio * 0.8
else:
    total = unidad * precio

print("El monto total de la compra es --> : $", total)

