# Objetivo: 
# Nombre y Apellido: Victor Luis CObeñas Blanco
# Fecha: 06/04/2025


#=======================================
# Ingresa un genero (M/F/O):
#
# Ud. es masculino
#
#=======================================

while(True):
    géneroIngresado = str(input("Ingrese un Género (M/F/O): "))
    if(géneroIngresado.upper() == 'M' or géneroIngresado.upper() == 'F' or géneroIngresado.upper() == 'O'):
        break
    print("ERROR DE USUARIO ............. Ingrese un Género (M/F/O)")
if(géneroIngresado == 'M'):
    print("El género ingreso es MASCULINO !")
elif(géneroIngresado == 'F'):
    print("El género ingreso es FEMENINO !")
else:
    print("El género ingreso OTROS !")
