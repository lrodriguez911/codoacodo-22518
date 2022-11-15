'''Iplementar una clase llmada persona q tendra atr (var) su nmobre y 2 metodos, 
uno de ellos inicializara el atr nombre y el sgte metodo mostrala en la pnatalla el contenido del mismo. 
Definir dos objetos de la clase Persona e incorporar una variable de la clase (piernas).
'''

class Persona:

    piernas = 2 #class attribute

    def inicializar(self, nombre):# Constructor method
        self.nombre = nombre #instance attribute
    
    def imprimir(self): # method to show data
        print(f'Nombre: {self.nombre}')

#Programa principal
persona1 = Persona() # we create an object based on the person class
persona1.inicializar("Lucas Rodriguez")
persona1.imprimir()

persona2 = Persona()
persona2.inicializar('Florencia')
persona2.imprimir()


persona1.piernas = 4 #changes attributes
persona2.nombre = 'Maria'
