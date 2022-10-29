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
            dev : 'Evan You',
            anio : '2014'
        }
    }
}).mount('#app1')