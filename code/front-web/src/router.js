import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
        },
        {
            path: '/video-face',
            name: 'videoFace',
            component: () => import('./views/VideoFace.vue')
        },
        {
            path: '/img-face',
            name: 'imgFace',
            component: () => import('./views/ImgFace.vue')
        },
        {
            path: '/thanks',
            name: 'thanks',
            component: () => import('./views/Thanks.vue')
        },
        {
            path: '/menu',
            name: 'menu',
            component: () => import('./components/Menu.vue')
        },

    ]
})
