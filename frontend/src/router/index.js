import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)


// input views
import LoginPage from "@/views/LoginPage";
import RegistrationPage from "@/views/RegistrationPage";
import AccountPage from "@/views/AccountPage";
import HomePage from "@/views/HomePage";


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
    {
        path: '/registration',
        name: 'registration',
        component: RegistrationPage
    },
    {
        path: '/account',
        name: 'account',
        component: AccountPage
    },
    {
        path: '/',
        name: 'home',
        component: HomePage
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
