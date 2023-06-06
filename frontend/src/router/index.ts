import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Home from '@/pages/home/index.vue'
import Homes from '@/components/Content/homes.vue'
import Project from '@/components/Content/project.vue'
import Info from '@/components/Content/info.vue'
import Contact from '@/components/Content/contact.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'home',
    component: Home,
    children: [
      {
        path: '/home',
        name: 'home',
        component: Homes
      },
      {
        path: '/project',
        name: 'project',
        component: Project
      },
      {
        path: '/info',
        name: 'info',
        component: Info
      },
      {
        path: '/contact',
        name: 'contact',
        component: Contact
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
