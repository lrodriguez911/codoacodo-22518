#instruccion print
print("Hola a todos!")
print()
print("Estamos aprendiendo python", end=' ')
print("en la comision 22518")#continua en la linea anterior
print(12 * 4)


nombre = 'Lucas Rodriguez'
print("hola", nombre)#'coma' deja espacio
print("hola" +  nombre)#'mas(+)' no deja espacio


edad = 30
print("hola! mi nombre es", nombre, "y tengo", edad, "años")
print("hola! mi nombre es", nombre, "y tengo"+ str(edad), "años")

print("Lucas", 37, 3.14, True, "San Miguel")
print()

#separadores
print(22, 55, 99 , sep= ' * ')# separador personalizado
print(22, 55, 99 , sep= ' \t ')#\t es una tab
print(22, 55, 99 , sep= ' \n ')#\n es un saldo de linea
print(22, 55, 99 , sep= ' \n ')#\n \n es un doble saldo de linea


print("Estamos aprendiendo python", end=' / ')
print("otra linea")
print("nueva linea")