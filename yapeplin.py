#1. Ud. va a yapear o plinear montos, Las Unicas opciones son "Y" y "P".
#2. Debera validar el ingreso de los montos (mayor a 0.00) a Ingresar (iteracciones)
#3. Debera utilizar variables de incremento y acumulacion
#4. Si utilizo la forma de pago YAPE tendra una comision de 0.12
#5. Si utilizo la forma de pago PLIN tendra una comision de 0.13
#6. El descuento sera afectado al total acumulado y total acumulado con descuento

#==============================================
# Ingrese una opcion de pago (Y/P) : P
#
# Ingrese a cantidad de depositos
#
# Ingrese monto 1: 10
# Ingrese monto 2: 20
# Ingrese monto 3: 30
#
#======== REPORTATE ============
# El monto acumulado es: 60
# EL monto acumulado con descuento es: 56
#==============================
#===============================================


#1. Ud. va a yapear o plinear montos, Las unicas opciones son "Y" y "P"
while(True):
    opcionIngresado = str(input("Ingrese una opcion de pago (Y/P): ")).upper()
    if (opcionIngresado == "Y" or opcionIngresado == "P"):
        break
    print("ERROR DE USUARIO......... Ingrese una opcion de pago (Y/P)")

#2. Debera validar el ingreso de los montos (mayo a 0.00) a Ingresar (iteracciones)
while(True):
    numeroIngresado = float(input("Ingrese un numero mayor a  0: "))
    if( numeroIngresado > 0.00):
        break
    print("ERROR DE USUARIO............. Ingrese un numero mayor a S/. 0")

#Respectiva
i=0
montoAcumulado = 0
while(i < numeroIngresado):
    i+= 1 # se incrementa en uno
    monto = float(input(f"\tIngrese un monto {i} :" ))
    montoAcumulado = montoAcumulado + monto
    if(opcionIngresado == "Y"):
        montoDcto = montoAcumulado * 0.12
    else:
        montoDcto = montoAcumulado * 0.13


print("======== REPORTATE ============")
print(montoAcumulado)
print(montoDcto)
print(montoAcumulado-montoDcto)
