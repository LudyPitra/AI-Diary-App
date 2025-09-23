<script setup>
import { RouterLink, RouterView, useRouter, useRoute } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const router = useRouter()
const route = useRoute()

const handleLogout = () => {
  authStore.logout()
  router.push('/login')
}
</script>

<template>
  <header v-if="route.path !== '/login'">
    <nav>
      <div v-if="!authStore.token">
        <RouterLink to="/login">Login</RouterLink>
      </div>
      <div v-else>
        <RouterLink to="/diary">Diário</RouterLink>
        <button @click="handleLogout">Logout</button>
      </div>
    </nav>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  padding: 1rem 2rem;
  line-height: 1.5;
}

nav {
  display: flex;
  justify-content: flex-end; /* Alinha os links à direita */
  align-items: center;
  font-size: 1rem;
}

nav a, nav button {
  font-weight: bold;
  color: #076a7e; /* Letras secundárias */
  text-decoration: none;
  margin-left: 1.5rem;
  transition: color 0.3s;
}

nav a:hover {
  color: #303030;
}

/* Estilo para o link da página ativa */
nav a.router-link-exact-active {
  color: #303030; /* Letras principais */
}

nav button {
  border: none;
  background: none;
  cursor: pointer;
  padding: 0;
  font-family: inherit; /* Usa a mesma fonte do resto */
  font-size: inherit;
}

nav button:hover {
  text-decoration: underline;
  color: #303030;
}
</style>