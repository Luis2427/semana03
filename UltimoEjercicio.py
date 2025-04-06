#Objetivo: Uso de todo lo apremdido
# 1. Validar el ingreso de un numero de 2 a 4 (enteros)
# 2. Validar el ingreeso con la opcion A 
# 3. Con el numero ingresado en el punto 1, realizar las interacciones en un while
# 4- Imprime la multiplicacion acumulativa
#Nombre: Cobeñas Blanco Victor Luis
#Fecha: 05/04/2025


# 1. Validar el ingreso de un numero de 2 a 4 (enteros)
while(True): 
   NUMERO = int(input("Usuario Ingresar un numero de 2 a 4: "))
   if(NUMERO >= 2 and NUMERO <=4):
    break  
   print("ERROR DE USUARIO ........... Ingrese un numero 2 a 4 !!!")
# 2. Validar el ingreeso con la opcion A 
while(True): 
   LETRA = str(input("Usuario Ingresar la letra A: "))
   if(LETRA .upper() == "A"):
    break  
   print("ERROR DE USUARIO ........... Ingrese la letra> (A) !!!")
# 3. Con el numero ingresado en el punto 1, realizar las interacciones en un while
i = 0                   
varAcumulacion = 1     
while( i <= 3):       
    monto = int(input("Ingrese un monto: "))
    varAcumulacion = varAcumulacion + monto 
    i += 1
#4- Imprime la multiplicacion acumulativa
print("Acumulacion es: ",varAcumulacion)    