'''Crear clase alumno: attr nombre y nota.
Definir methods to inicialize your attributes, prit and show a msg that show: Promociono(nota >=7
'''


class Alumno:

    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f'{self.nombre} su nota es {self.nota}')


    def mostrar_estado(self):
        if self.nota >= 7:
            print('promociono')
        elif self.nota >= 4:
            print('rinde final')
        else:
            print('desaprobo')


student1 = Alumno()
student2 = Alumno()
student3 = Alumno()

student1.inicializar('Lucas Rodriguez', 10)
student2.inicializar('Alberto Sanchez', 6)
student3.inicializar('Juan Manuel', 2)

student1.imprimir()
student1.mostrar_estado()
student2.imprimir()
student2.mostrar_estado()
student3.imprimir()
student3.mostrar_estado()


class Alumno_:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota