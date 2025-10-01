<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';

// Reactive variables for the email and password fields.
const email = ref('');
const password = ref('');

// Get the auth store and router instances.
const authStore = useAuthStore();
const router = useRouter();

/**
 * Handles the login form submission.
 */
const handleLogin = async () => {
  // Call the login action from the auth store.
  await authStore.login(email.value, password.value);

  // If login is successful (token exists), redirect to the home page.
  if (authStore.token) {
    router.push('/');
  }
};
</script>

<template>
  <div class="back-button-container">
  <RouterLink to="/" class="back-button" aria-label="Back to Home">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <line x1="19" y1="12" x2="5" y2="12"></line>
      <polyline points="12 19 5 12 12 5"></polyline>
    </svg>
  </RouterLink>
</div>
<main>
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="email">Email</label>
        <input v-model="email" type="email" id="email" placeholder="email@example.com" />
      </div>
      <div>
        <label for="password">Password</label>
        <input v-model="password" type="password" id="password" placeholder="Your password" />
      </div>
      <div v-if="authStore.error" class="error-message">{{ authStore.error }}</div>
      <button type="submit">Login</button>
    </form>
  </main>
</template>


<style scoped>

.back-button-container {
  position: absolute;
  top: 1.5rem;
  left: 1.5rem;
  z-index: 10;
}

.back-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 50%; /* Deixa o fundo redondo */
  color: #076a7e; /* Cor da seta */
  background-color: transparent;
  transition: background-color 0.3s ease;
}

.back-button:hover {
  background-color: #ffffff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

main {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #ecfeff; /* plano de fundo #1 */
  font-family: sans-serif;
}

form {
  background-color: #ffffff; /* plano de fundo #2 */
  padding: 40px;
  border-radius: 12px; /* Bordas arredondadas */
  box-shadow: 0 10px 18px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

h1 {
  color: #303030; /* letras principais */
  margin-bottom: 24px;
  text-align: center;
}

div {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 8px;
  color: #076a7e; /* letras secundárias */
  font-weight: bold;
}

input {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 8px; /* Bordas arredondadas */
  box-sizing: border-box; /* Garante que o padding não aumente a largura */
  color: #303030;
}

/* Dentro de <style scoped> em LoginView.vue */

/* ... (seus estilos existentes para input) ... */

input:focus {
  outline: none; /* Remove o outline padrão do navegador */
  border-color: #076a7e; /* Define a cor da borda para a cor de destaque */
  box-shadow: 0 0 0 2px #d1f1f2; /* Adiciona um brilho suave com a cor de sombra */
}

input::placeholder {
  color: #828282; /* letras de exemplo */
}

button {
  width: 100%;
  padding: 12px;
  background-color: #076a7e; /* Cor secundária para o botão */
  color: #ffffff;
  border: none;
  border-radius: 8px; /* Bordas arredondadas */
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 0 0 0 #d1f1f2; /* Sombra/brilho inicial transparente */
}

button:hover {
  /* Destaque ao redor quando o mouse estiver em cima */
  box-shadow: 0 0 0 4px #d1f1f2; 
}

.success-message {
  color: #076a7e;
  background-color: #d1f1f2;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 20px;
  text-align: center;
}

.error-message {
  color: #D8000C;
  background-color: #FFD2D2;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 20px;
  text-align: center;
}
</style>