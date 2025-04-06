#Objetivo: Uso de variable Acumulacion
#Nombre: Cobeñas Blanco Victor Luis
#Fecha: 05/04/2025

i = 0                   # variable de incremento
varAcumulacion = 0      # variable de acumulacion
while( i <= 3):         # mientras (que sean menores o igual a 3)
    monto = int(input("Ingrese un monto: ")) # solicitando un monto entero
    varAcumulacion = varAcumulacion + monto  # Acumulando los montos en la variable varAcumulacion
    i += 1
print("Acumulacion es: ",varAcumulacion)     # Imprimiendo el resultado del acumulado