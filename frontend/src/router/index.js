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
        component: HomePage,
        meta: {
            title: 'Путешествуй по России!'
        }
    },
    {
        path: '/login',
        name: 'login',
        component: LoginPage,
        beforeEnter: (to, from, next) => {
            if (Vue.$cookies.isKey('Token'))
                next('/')
            else
                next()
        },
        meta: {
            title: 'Логин'
        },
    },
    {
        path: '/registration',
        name: 'registration',
        component: RegistrationPage,
        beforeEnter: (to, from, next) => {
            if (Vue.$cookies.isKey('Token'))
                next('/')
            else
                next()
        },
        meta: {
            title: 'Регистрация'
        }
    },
    {
        path: '/account',
        name: 'account',
        component: AccountPage,
        meta: {
            title: 'Профиль'
        },
        beforeEnter: (to, from, next) => {
            if (!Vue.$cookies.isKey('Token'))
                next('/')
            else
                next()
        },
    },
    {
        path: '/search',
        name: 'search',
        component: SearchPage,
        meta: {
            title: 'Поиск тура'
        }
    },
    {
        path: '/booking',
        name: 'booking',
        component: TourBookingPage,
        meta: {
            title: 'Бронированние'
        },
        beforeEnter: (to, from, next) => {
            if (to.query.id === undefined)
                next('/')
            else
                next()
        },
    },
    {
        path: '/favorites',
        name: 'favorites',
        component: FavoritesPage,
        meta: {
            title: 'Избранное'
        },
        beforeEnter: (to, from, next) => {
            if (!Vue.$cookies.isKey('Token'))
                next('/')
            else
                next()
        },
    },
    {
        path: '/tour',
        name: 'tour',
        component: TourPage,
        meta: {
            title: 'Туры'
        }
    },
    {
        path: '*',
        name: 'notfound',
        component: NotFoundPage,
        meta: {
            title: 'Страница не найдена'
        }
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

router.beforeEach((to, from, next) => {
    document.title = to.meta.title
    next()
});

export default router