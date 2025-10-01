// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue' 
import DiaryView from '../views/DiaryView.vue' 

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  // Defines the application's routes.
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },

    {
      path: '/login',
      name: 'login',
      component: LoginView
    },

    {
      path: '/diary',
      name: 'diary',
      component: DiaryView,
      // This route requires authentication.
      meta: { requiresAuth: true }
    }
  ]
})

// Navigation guard to protect authenticated routes.
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  const requiresAuth = to.meta.requiresAuth;

  // Redirect to login if the route requires auth and the user is not authenticated.
  if (requiresAuth && !authStore.token) {
    next({ name: 'login' });
  } else {
    next();
  }
});

export default router