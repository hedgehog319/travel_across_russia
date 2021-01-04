import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)


// input views
import LoginPage from "@/views/LoginPage";


const routes = [
    // {
    //     path: '/',
    //     name: 'Home',
    //     component: App
    // },
    {
        path: '/login',
        name: 'login',
        component: LoginPage
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
