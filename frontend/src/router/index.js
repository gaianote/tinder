import Vue from 'vue'
import VueRouter from 'vue-router'
import flow from "@/pages/flow.vue";
import mock from "@/pages/mock.vue";

Vue.use(VueRouter)

const routes = [
    { path: '/flow', component: flow },
    { path: '/mock', component: mock },
]
  
const router = new VueRouter({
    routes 
})

export default router
