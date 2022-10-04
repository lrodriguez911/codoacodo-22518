//Crear objetos a través de literales { }
let coche = {
    marca: "Ford",
    tipo: "Ranger",
    modelo: 2019,
    portaequipajes: true,
    caracteristicas: function(){
        return this.marca + " " + this.tipo + " (" + this.modelo + ")"
    },
    caracteristicasDos(){
        return "Año: "+this.modelo+"\nMarca: "+this.marca+"\nNombre: "+this.tipo
    }
}

//Programa principal
console.log(coche)
console.log("Modelo:", coche.modelo) //objeto.propiedad
console.log("Marca:", coche.marca) //objeto.propiedad

//Cambiar valores de la propiedad
coche['modelo'] = 2022
//coche['marca'] = "Renault"
console.log("Modelo:", coche.modelo) //objeto.propiedad
console.log("Marca:", coche.marca) //objeto.propiedad
console.log(coche.caracteristicas())
if (coche.portaequipajes){
    console.log("La",coche.marca,coche.tipo,"tiene portaequipajes")
}
console.log(coche.caracteristicasDos())

