import { defineStore } from 'pinia'
import axios from 'axios'

// Defines the authentication store for Pinia.
export const useAuthStore = defineStore('auth', {
    state: () => ({
        // The authentication token. Retrieved from localStorage to persist login state.
        token: localStorage.getItem('authToken') || null,
        // Holds any error messages from login attempts.
        error: null
    }),
    actions: {
        /**
         * Logs in a user by fetching an authentication token from the API.
         * @param {string} email - The user's email.
         * @param {string} password - The user's password.
         */
        async login(email, password) {
            this.error = null; // Reset error state before a new login attempt.
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
        /**
         * Logs out the current user.
         */
        logout() {
            // Clear the token from state and localStorage.
            this.token = null;
            localStorage.removeItem('authToken');
        }
    },                    
})