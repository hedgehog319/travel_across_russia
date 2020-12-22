import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueAxios from 'vue-axios'


// eslint-disable-next-line @typescript-eslint/ban-ts-ignore
// @ts-ignore
import Vuelidate from 'vuelidate'

// eslint-disable-next-line @typescript-eslint/ban-ts-ignore
// @ts-ignore
import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

Vue.use(VueAxios, axios)
Vue.use(VueMaterial)
Vue.use(Vuelidate)

Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')
