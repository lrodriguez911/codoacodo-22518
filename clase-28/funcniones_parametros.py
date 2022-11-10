#Funciones con parametros
# parametros: al definir la funcion 
# argumentos: al invocar la funcion

# funciones con un parametro
def imprimir_mensaje_n_veces(n):
    for i in range(n):
        print("Mensaje")

# fucnion con mas de un parametro
def imprimir_mensaje_personalizado(n, msj):
    for i in range(n):
        print(msj)


times = int(input("Cuantas veces vas a imprimir?"))
while times <=0:
    print("Date not valid")

# imprimir_mensaje_n_veces
msj = input("which is the message: ")
while len(msj) == 0:
    print("Insert a valid number")
    msj = input("which is the message")