const { createApp } = Vue
createApp({
    data() {
        return {
            mensaje: 'Hola Mundo con Vue!',
            curso: 'Codo a Codo',
            profesor: 'Juan Pablo',
            descripcion: 'Vue.js es un framework (v-text)',
            subtitulo: `<h2>Esto es un subtitulo agregado con 
            <span class="naranja">v-html </span></h2>`,
            foto:'logovue.png',
            url: 'https://vuejs.org/',
            claseCSS: 'enlace',
            oculto: false,//false oculta un elemento , true lo muestra
            otro_titulo:'Soy otro titulo'
        }
    }
}).mount('#app')