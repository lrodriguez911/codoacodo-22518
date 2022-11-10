print("****** CADENAS DE CARACTERES ******")
#Escritura y concatenación
'''string1 = "Aprendiendo cadenasde caracteres"
string2 = 'en codo a codo'
print(string1)
print(string2)
print(string2 , 'concatenando')
print(string2 + 'concatenando')'''


#Concatenar números y cadenas
# edad = 30
# altura = 1.80
# datos = "La edad es " + str(edad)  + " años y la altura es " + str(altura)
# print(datos)



# Combinar comillas simples y dobles
# print("Hola a todos 'como estan'")
# print('Hola a todos "como estan"')



#Replicación de cadenas
# risa = 'ja'
# carcajada = risa*5
# print(risa)
# print('-'*10)


#Cadenas multilínea
# string = """strings 
# multilineas """
# strings2 = '''strings 
# multilineas con comillas
#  simples'''

#Comparación de cadenas (ASCII y case sensitive)
# str1 = "@" #alt + 64 ascii 64
# str2 = "^" #alt + 94 ascii 94
# str3 = "@" #alt + 64 ascii 64
# print(str1 >  str2)
# print(str1 <  str2)
# print(str1 ==  str3)

# city = "Cordoba"
# if city == "Cordoba":
#     print("El envio llegara mañana")
# else:
#     print("El envio llega pasado mañana")


#Largo de cadenas y subíndices
# name = "Lucas"
# print(len(name))
# print(name[0])
# print(name[-1])
# print(name[len(name) - 1])


#Métodos upper / lower / capitalize / title
# str = "learning python"
# print(str.upper())
# print(str.lower())
# print(str.capitalize())
# print(str.title())


#Rebanadas (slicing)
# [:] Todos los elementos.
'''str = "learning python"
print(str[:])

# [start:] Todos los elementos desde el índice establecido(start).
print(str[1:])

# [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
print(str[:0])

# [start:end] Todos los elementos de un rango de índices.
print(str[0:2])

# [start:end:step] Todos los elementos de un rango de índices con saltos.
print(str[0:5:2])

# [::step] Todos los elementos con saltos.
print(str[::2])

# [::step] Todos los elementos con saltos (negativo).
print(str[::-1])'''



#Operadores de pertenencia: in / not in
'''str = "learning python"
print("l" in str)
print("learning" in str)
print("D" in str)
print("L" not in str)
print("D" not in str)'''




#Iterando cadenas
#For
'''str = "Python"
for letra in str:
    # 'print(letra)'
    print(letra, end='L')'''

#While

'''str = "python"
i = 0
while i < len(str):
    print(str[i])
    # print(str[1], end='*')
    i += 1'''


#Uso de min y max
str = "Python"
print(min(str)) #ascii
print(max(str)) #ascii