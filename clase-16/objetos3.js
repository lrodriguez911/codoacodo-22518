// Creación de objetos a partir de clases
class Animal{ //Creamos la clase: molde de objetos
    constructor(nombre, edad, vivo, color){
        this.nombre = nombre
        this.edad = edad
        this.vivo = vivo
        this.color = color
    }
    comer(){return this.nombre+" está comiendo"}
}

//Instanciamos dos objetos de la clase Animal:
let gato = new Animal("Pepe",5,true,"Marrón")
let elefante = new Animal("Dumbo", 30, false,"Gris")

console.log(gato.nombre)
console.log(elefante.edad)
console.log(gato.comer())
console.log(elefante.comer())
gato.nombre = "Michifus"
elefante.edad = 20
elefante.vivo = true
console.log(gato)
console.log(elefante)

