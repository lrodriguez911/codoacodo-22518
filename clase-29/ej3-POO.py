'''Make a class that represent a Animal. Define like attibutes'''


class Animal:
    def __init__(self, nopmbre, tipo, edad):
        self.nombre = nopmbre
        self.tipo = tipo
        self.edad = edad

    def imprimir(self):
        print(f'Tipo: {self.tipo}\n Nombre:{self.nombre}\nEdad: {self.edad}')

    def __str__(self):
        return f'Tipo: {self.tipo}\nNombre:{self.nombre}\nEdad: {self.edad}'

    def __del__(self):
        return f'{self.nombre} fue eliminado'

#programa principal
animal_1= Animal("Tomy", "Perro", 5)

print(animal_1)