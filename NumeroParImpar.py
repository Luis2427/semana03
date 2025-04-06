# Objetivo Realizar un programa que te solicite el ingreso de un número mayor a 10 y menor a 50
#          Y QUE TE IMPRIMA SI ES UN NUMERO PAR O IMPAR, utiliza MOD.
# Nombre y Apellido: Victor Luis CObeñas Blanco
# Fecha: 06/04/2025

#=======================================
# Ingresa un número mayor a 10 y menor a 50:
#
# El número es par
#
#=======================================

while(True):
    númeroIngresado = int(input("Ingrese un número mator a 10 y menor a 50: "))
    if(númeroIngresado > 9 and númeroIngresado < 51):
        break
    print("ERROR DE USUARIO ............. Ingrese un número mayor a 10 y menor a 50")

if(númeroIngresado % 2 == 0): 
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")