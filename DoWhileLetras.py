#Objetivo: Uso de DoWhile (HACER - mientras)
#Nombre: Cobeñas Blanco Victor Luis
#Fecha: 05/04/2025


while(True): 
   LETRA = str(input("Usuario Ingresar una opcion (A/B/C): "))
   if(LETRA.upper == "A" or LETRA.upper == "B" or LETRA.upper == "C"):
    break  
   print("ERROR DE USUARIO ........... Ingresar una opcion (A/B/C) !!!")

print("ok saliste del bucle")