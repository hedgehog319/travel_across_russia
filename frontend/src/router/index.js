import Vue from 'vue'
import VueRouter from 'vue-router'
// input views
import LoginPage from "@/views/LoginPage";
import RegistrationPage from "@/views/RegistrationPage";
import AccountPage from "@/views/AccountPage";
import HomePage from "@/views/HomePage";
import SearchPage from "@/views/SearchPage";
import TourBookingPage from "@/views/TourBookingPage";
import FavoritesPage from "@/views/FavoritesPage";
import NotFoundPage from "@/views/NotFoundPage";
import TourPage from "@/views/TourPage";

Vue.use(VueRouter)


const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage
    },
    {
        path: '/login',
        name: 'login',
        component: LoginPage,
        beforeEnter: (to, from, next) => {
            if (Vue.$cookies.isKey('Token'))
                next('/')
        }
    },
    {
        path: '/registration',
        name: 'registration',
        component: RegistrationPage,
        beforeEnter: (to, from, next) => {
            if (Vue.$cookies.isKey('Token'))
                next('/')
        }
    },
    {
        path: '/account',
        name: 'account',
        component: AccountPage
    },
    {
        path: '/search',
        name: 'search',
        component: SearchPage
    },
    {
        path: '/booking',
        name: 'booking',
        component: TourBookingPage
    },
    {
        path: '/favorites',
        name: 'favorites',
        component: FavoritesPage
    },
    {
        path: '/tour',
        name: 'tour',
        component: TourPage
    },
    {
        path: '*',
        name: 'notfound',
        component: NotFoundPage
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router