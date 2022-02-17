import { createApp } from 'vue'
import router from './router.js'
import store from './store.js'
import inputs from './components/global/index'
import axios from 'axios'

import App from './App.vue'

const app = createApp(App)

app.config.productionTip = false

// connect components
let components = [...inputs]
components.forEach((component) => {
  app.component(component.name, component)
})

app.config.globalProperties.$axios = axios

// directives
app.directive('click-outside', {
  beforeMount(el, binding) {
    el.clickOutsideEvent = function (event) {
      // here I check that click was outside the el and his childrens
      // console.log(el, event.target)
      if (el==event.target) {
        // Если кликнули на элемент на котором записана директива
      }
      
      if (el.contains(event.target)) {
        // если кликнули на элемент, который находится внутри директивы
      }
      if (!(el===event.target || el.contains(event.target))) {
        // console.log('click on background')
        // вызов функции, переданной через имя в директиву
        binding.value()
      }
    };
    document.body.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted: function (el) {
    document.body.removeEventListener('click', el.clickOutsideEvent)
  }
})

app.use(store).use(router).mount('#app')
