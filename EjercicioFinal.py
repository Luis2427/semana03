#1. Ud. va ingresar una cantidad de notas )ITERACCIONES.
#2. Debera validar el ingreso de la cantidad (DO-WHILE)
#3. Debera utilizar variables de incremento y acumulacion
#4. Debera acumular las notas y promediarlas
#5. Resultado
#6. Ud. ingreso n notas
#    la suma de notas es: m
#   EL promedio de las notas es: P


# Ingrese una cantidad de notas (ITERACCIONES): 3
#   Ingrese nota 1: 15
#   Ingrese nota 2: 16
#   Ingrese nota 3: 17
# ====RESULTADO=====
# Ud. ingreso 3 notas
# La suma de las notas es: 48
# El promedio de las notas es: 16.00

#1. Ud. va ingresar una cantidad de notas )ITERACCIONES.
while(True):
    cantnot = float(input("Ingrese la cantidad de notas): "))
    if (cantnot <= 3):
        break
    print("ERROR DE USUARIO......... Ingrese la cantidad de notas)")
while(True):
    numeroIngresado = float(input("Ingrese las notas: "))
    if( numeroIngresado > 2 and numeroIngresado < 4):
        break
    print("ERROR DE USUARIO............. Ingrese las notas")
i=0
montoAcumulado = 0
while(i < numeroIngresado):
    i+= 1 # se incrementa en uno
    numeroIngresado = float(input(f"\tIngrese Nota {i} :" ))
    numeroIngresado = montoAcumulado + cantnot
    if(nota > 0)
        ingresoDeNotas = numeroIngresado+montoAcumulado
    else:
        ingresoDeNotas = montoAcumulado % 3 

print("======== RESULTADO ============")
print(numeroIngresado)
print(montoAcumulado)
pritn(promedio)