const { createApp } = Vue
createApp({
    data() {
        return {
          titulo:'Productos',
          productos:['tablet', 'celulares', 'consolas'],
          productos2:[
            {nombre: 'Silla', cantidad:5},
            {nombre: 'Mesa', cantidad:10},
            {nombre: 'Cama', cantidad:15}
          ]
        }
    }
}).mount('#app')