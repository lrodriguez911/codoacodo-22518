'''10. Definir una superclase Vehículo con dos atributos: color y ruedas, agregar sus métodos init
y str. Agregar un método que informe en cuántas ruedas está andando el vehículo.
Definir una subclase Transporte que herede de Vehículo e incorpore los atributos
velocidad y modelo, agregar sus métodos init y str considerando los atributos heredados.
En el programa principal instanciar tres objetos, uno de ellos de la superclase Vehículo con
sus 2 atributos. Los otros dos serán un coche y una moto, con sus 4 atributos (los propios y
los heredados). Imprimir los 3 objetos'''


class Vehicle: #superclass
    def __init__(self, color, wheel):
        self.color = color #atr of instance
        self.wheel = wheel #atr of instance
    def __str__(self):
        return f'Color: {self.color}\nWheels: {self.wheel}'

    def move(self):
        print(f'I am ridding in {self.wheel} wheels')

class Trasnport(Vehicle):
    
    def __init__(self, color, wheel, velocity, model):
        Vehicle.__init__(self, color, wheel) # atr inherited
        self.velocity = velocity # own atr
        self.model = model # own atr

    def __str__(self):
        return Vehicle.__str__(self) + f'\nVelocit: {self.velocity} km/h \nModel: {self.model}' # showing atr inherited and own


#Main program 

vehicle1= Vehicle("Red", 4)
print(vehicle1)
vehicle1.move()


car1 = Trasnport("yellow", 4 , 150, "Ford")
print(car1)
car1.move()

moto1 = Trasnport("black", 2, 180, "Yamaha")
print(moto1)
moto1.move()
print(moto1)
