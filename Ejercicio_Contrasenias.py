contador = 0
uno = int (input("Bienvenido confirme por favor, su clave es 1--Alfabetica o  2--Numerica ? "))
if uno == 1:
    contrasenia = str(input("\n Ingrese su contrasenia por favor: \n"))
    ingreso2 = str(input("Reingrese su contrasenia por favor\n"))

if contrasenia == ingreso2:
    print("---------- La contrasenia ingresada es Correcta ----------")
    print("----------------------------------------------------------------------\n")
else:
    print("########## La contrasenia es INCORRECTA ##########\n")
    contador += 1
while contador >= 3:
        print("CUENTA BLOQUEADA, COMUNIQUESE CON EL BANCO PARA GESTIONAR EL DESBLOQUEO\n\n")
