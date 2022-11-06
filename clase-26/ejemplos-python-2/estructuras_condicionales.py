# ESTRUCTURAS CONDICIONALES
# if 
# EJERCICIO: Ingresar un número y determinar si es menor que 10.

'''num = int(input('Ingrese un numero: '))
if num < 10:
    print("Numero menor que 10")
print("Fin")'''

# if .. else
# EJERCICIO: Ingresar un número distinto de cero y decir si es par o impar.
'''num = int(input("Ingresar numero distinto de cero: "))
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero no es par")'''



# Estructuras condicionales anidadas / if .. elif .. else
# EJERCICIO: Ingresar un número entero e imprimir un mensaje indicando si es cero, par o impar.
'''num = int(input("Ingrese un numero: "))

if num == 0:
    print("Es cero")
elif num % 2 == 0:
    print("Es par")
else:
    print('Es impar')
'''


# Leer un número entero e imprimir un mensaje de acuerdo al valor ingresado:
# a) Si ingresa 1 debe mostrar “Ingresando a depósitos…” 
# b) Si ingresa 2 debe mostrar “Ingresando a extracciones…”
# c) Si ingresa 3 debe mostrar “Pago de tarjeta”
# d) En el caso de ingresar otro número debe aparecer “Opción incorrecta”.

'''op = int(input('ingrese una opcion : '))
if op == 1:
    print('Ingresando a depósitos…')
elif op == 2:
    print('Ingresando a extracciones...')
elif op == 3:
    print('Ingresando a depósitos…')
else:
    print('Opcion incorrecta')'''


# Uso de operadores lógicos (AND y OR)
# AND
# EJERCICIO: Ingresar un número y decir si tiene de dos cifras o no.
 
num = int(input('ingrese un numero'))
if num >= 10 and num <= 99:
    print('el numero tiene 2 cifras')
else:
    print('el numero no tiene 2 cifras')
# OR
# EJERCICIO: Ingresar un número entero y decir si es divisible por 6 o 2

