import { defineStore } from 'pinia'
import axios from 'axios'

export const useAuthStore = defineStore('auth', {
    state: () => ({
        token: localStorage.getItem('authToken') || null,
        error: null
    }),
    actions: {
        async login(email, password) {
            this.error = null;
            try {
                const response = await axios.post('http://localhost:8000/token', {
                    email: email,
                    password: password
                });

                this.token = response.data.access_token;
                localStorage.setItem('authToken', this.token);
                console.log("Login successful, stored token: ", this.token);

            } catch (error) {
                console.error("Login failed: Email or password is incorrect");
                console.error("Login failed: ", error);
            }
        },
        logout() {
            this.token = null;
            localStorage.removeItem('authToken');
        }
    },                    
})