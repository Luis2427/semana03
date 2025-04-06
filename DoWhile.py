#Objetivo: Uso de DoWhile (HACER - mientras)
#Nombre: Cobeñas Blanco Victor Luis
#Fecha: 05/04/2025


while(True): 
   NUMERO = int(input("Usuario Ingresar un numero entero positivo: "))
   if((NUMERO > 0 and NUMERO <19) or (NUMERO > 29 and NUMERO <61)):
    break  
   print("ERROR DE USUARIO ........... Ingrese un numero > 0 !!!")

print("ok saliste del bucle")