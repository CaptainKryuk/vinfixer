import { createRouter, createWebHistory } from "vue-router"

export default createRouter({
  mode: 'history',
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: () => import('@/components/pages/Main.vue')
    },
    {
      path: '/login',
      component: () => import('@/components/pages/account/Login.vue')
    },
    {
      path: '/register',
      component: () => import('@/components/pages/account/Register.vue')
    },
    {
      path: '/contacts',
      component: () => import('@/components/pages/Contacts.vue')
    },
    

    { path: '/:pathMatch(.*)*', name: 'NotFound', component: () => import('@/components/pages/utils/NotFound.vue')}
  ]
})