const storage = window.localStorage

const check = document.querySelector('.botonespacio')
const body = document.querySelector('.body')

let oscuro = Boolean(storage.getItem('oscuro'))

const comprobarOscuro = oscuro => {
  if (oscuro) {
    body.classList.add('cambio-color')
    check.checked = true
  }else{
    body.classList.remove('cambio-color')
    check.checked = false
  }
}
comprobarOscuro(oscuro)

check.addEventListener('click', function(){
  if (this.checked) {
    body.classList.add('cambio-color')
    storage.setItem('oscuro', true)
  }else{
    body.classList.remove('cambio-color')
    storage.removeItem('oscuro')
  }
}
)