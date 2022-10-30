const {createApp} = Vue
createApp({
    data(){
        return{
            msg : 'Mensaje escrito con Vue3',
            vue : 'VUE3'
        }
    }
}).mount('#app')
createApp({
    data(){
        return{
            titulo: '<h1>Hola <sapn class="clase">Mundo</span></h1>'
        }
    }
}).mount('#app1')
createApp({
    data(){
        return{
            claseCSS: 'nuevaClase',
            url: 'https://www.google.com.ar/'
        }
    }
}).mount('#app2')