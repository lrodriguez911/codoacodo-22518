/************** OTROS METODOS PARA ARRAYS *****************/

/*.forEach(cb, arg): Realiza la operación definida en cb por cada elemento del array.*/

var frutas = ["Banana", "Naranja", "Manzana", "Mango"]
document.write("FOR EACH <br>")
function mostrar(elemento, indice) {
    document.write(indice + ": " + elemento + "<br>")
}
frutas.forEach(mostrar)

/*.every(cb, arg): Comprueba si todos los elementos del array cumplen la condición de cb.*/

document.write("<br> EVERY <br>")
function compruebaEdad(edad) {
    return edad >= 18
}
var edades = [32, 33, 16, 40]
var edades2 = [32, 33, 20, 40]
document.write("Todos mayores?: ", edades.every(compruebaEdad))//false
document.write("<br>")
document.write("Todos mayores?: ", edades2.every(compruebaEdad))//true
document.write("<br>")

/*.some(cb, arg): Comprueba si al menos un elem. del array cumple la condición de cb.*/

document.write("<br> SOME <br>")
function compruebaNombre(nombre) {
    return nombre == "Lucas"
}
var nombres = ["Juan", "Mateo", "Camilo", "Lucas"]
var nombres2 = ["Juan", "Ana", "Luisa", "Mateo", "Camilo"]
document.write("Algún Lucas?: ", nombres.some(compruebaNombre))//true
document.write("<br>")
document.write("Algún Lucas?: ", nombres2.some(compruebaNombre))//false
document.write("<br>")

/* .map(cb, arg): Construye un array con lo que devuelve cb por cada elemento del array.*/

document.write("<br> MAP <br>")
var numeros = [4, 9, 16, 25]
function raizCuadrada(numero) {
    return Math.sqrt(numero)
}
function potencia(numero) {
    return numero*numero
}
function dobles(numero) {
    return numero+numero
}
document.write(numeros, "<br>")
document.write("<br>")
document.write("Raiz cuadrada: ", numeros.map(raizCuadrada))
document.write("<br>")
document.write("Potencia: ", numeros.map(potencia))
document.write("<br>")
document.write("Dobles: ", numeros.map(dobles))
document.write("<br>")

/*.filter(cb, arg): Construye un array con los elementos que cumplen el filtro de cb.*/

document.write("<br> FILTER <br>")
function personasComiezaEnP(persona) {
    return persona[0] == "P"
}
var personas = ["Ana", "Pablo", "Pedro", "Paola", "Horacio"]
document.write("Personas que comienzan con P: ", personas.filter(personasComiezaEnP))
document.write("<br>")

/*.findIndex(cb, arg): Devuelve la posición del elemento que cumple la condición de cb.*/

document.write("<br> FIND INDEX <br>")
function compruebaMenorEdad(edad) {
    if (edad < 18) {
        return edad
    }
}
var edades3 = [30, 19, 10, 28]
document.write("Posición menor de edad: ", edades3.findIndex(compruebaMenorEdad))
document.write("<br>")

/*.find(cb, arg): Devuelve el elemento que cumple la condición de cb.*/

document.write("<br> FIND <br>")
function compruebaMenorEdad(edad) {
    if (edad < 18) {
        return edad
    }
}
var edades4 = [25, 24, 19, 10, 28]
document.write("Edad del menor de edad: ", edades4.find(compruebaMenorEdad))
document.write("<br>")

/*.reduce(cb, arg): Ejecuta cb con cada elemento (de izq a der), acumulando el resultado.*/
/*.reduceRight(cb, arg): Idem al anterior, pero en orden de derecha a izquierda.*/

document.write("<br> REDUCE y REDUCE RIGHT <br>")
function restaPrecios(total, p) {
    return total - p
}
var precios = [110, 10, 25, 50, 15]
document.write("Reduce: ", precios.reduce(restaPrecios))
document.write("<br>")
document.write("Reduce right: ", precios.reduceRight(restaPrecios))
document.write("<br>")