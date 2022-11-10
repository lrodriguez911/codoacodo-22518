def sumar (a = 5, b = 8):
    return a + b


print(sumar(2 , 6))
print(sumar(2))
print(sumar(4))
# print(sumar(,5)) 


def saludar(name, msg = "nice to meet"):
    return print(f'Hi {name} {msg}')

saludar('lucas')
print('---------------------------')
saludar(msg = "Como estas?", name="Peter")
saludar(name= "Mary", msg="Welcome to elbow to elbow")
saludar("Jhon", msg="Whats is the weather")


