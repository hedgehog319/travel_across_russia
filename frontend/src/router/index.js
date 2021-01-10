import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)


// input views
import LoginPage from "@/views/LoginPage";
import RegistrationPage from "@/views/RegistrationPage";
import ProfilePage from "@/views/ProfilePage";


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
        path: '/tt',
        name: 'profile',
        component: ProfilePage
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
