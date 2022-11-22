'''9. Definir una clase Padre con un atributo apellido inicializado a través del método __init__().
También tendrá un método propio. Definir una clase hijo que herede de la clase Padre y
tenga un atributo de clase nombre (cadena de longitud 0) y un método propio.
En el programa principal instanciar un hijo, asignarle un nombre y llamar a su método y al
método del padre. Finalmente mostrar el nombre y apellido del hijo.'''


class Father():
    def __init__(self):
        self.lastName = "Rodriguez"

    def take(self):
        print(f'Dad come to the college')

class Son(Father): 
    name = ""

    def study(self):
        print(f'I am {self.name} and i am studying in codo a codo')

#Main program

son1 = Son()
son1.name = 'Lucas Maxi'
son1.take()
son1.study()
print(f'{son1.name} {son1.lastName}')