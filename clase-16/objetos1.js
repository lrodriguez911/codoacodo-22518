//Creación de objetos a través operador de asignación y new Object()
let vivienda = new Object() //Careamos el objeto
console.log(vivienda) //objeto vacío

//Creamos propiedades para el objeto vivienda
vivienda.calle = "Av. Rivadavia" //objeto.propiedad
vivienda.altura = 12345
vivienda.ambientes = 3

//Creamos métodos (funciones) para el objeto
vivienda.mostrarDomicilio = function(){ //objeto.método
    console.log("La vivienda está ubicada en:", vivienda.calle,vivienda.altura)
}//Función anónima

//Programa principal
vivienda.mostrarDomicilio() //Llamamos al método del objeto vivienda
console.log("La vivienda tiene:",vivienda.ambientes,"ambientes") //Mostramos una propiedad
