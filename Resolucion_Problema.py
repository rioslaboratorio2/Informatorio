
sexo=input("Ingrese Su Sexo  M (masculino)--- F (femenino)-->\t")
nombre=input("Ingrese su Nombre-->\t")

if sexo== "F" and sexo=="f":
     if nombre.lower() < "m":  # lo que hace el .lower es transformar el string completo que ingresa el usuario a Minuscula#
        grupo = "A"
     else:
         grupo= "B"
else:
    if nombre.lower()>"n":
        grupo="A"
    else:
        grupo = "B"

print("Usted pertenece al grupo:\t",grupo)


