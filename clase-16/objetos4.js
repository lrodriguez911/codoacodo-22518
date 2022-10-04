// Creación de objetos a través de una función constructora

function Persona(nombre, apellido, domicilio){
    this.nombre = nombre
    this.apellido = apellido
    this.domicilio = domicilio
}

//Creamos objetos de tipo Persona
let persona1 = new Persona("Juan", "Pérez","Av. Callao 123")
let persona2 = new Persona("Ana", "González","Av. Callao 125")
console.log(persona1.nombre,"vive en",persona1.domicilio)
console.log(persona2.nombre,"vive en",persona2.domicilio)