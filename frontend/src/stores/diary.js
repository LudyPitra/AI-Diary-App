import { defineStore } from 'pinia'
import axios from 'axios'
import { useAuthStore } from './auth'

// Defines the diary store for Pinia, managing diary entries.
export const useDiaryStore = defineStore('diary', {
  state: () => ({
    // Holds the list of diary entries for the current user.
    entries: [],
    // Holds any error messages from API calls.
    error: null,
  }),
  actions: {
    /**
     * Fetches all diary entries for the authenticated user from the API.
     */
    async fetchEntries() {
      const authStore = useAuth.Store()

      // Ensure the user is authenticated before fetching entries.
      if (!authStore.token) {
        this.error = 'User not authenticated.';
        return
      }

      this.error = null;
      try {
        const response = await axios.get('http://localhost:8000/entries', {
          headers: {
            'Authorization': `Bearer ${authStore.token}`
          }
        });
        
        // Update the state with the fetched entries.
        this.entries = response.data;

      } catch (error) {
        console.error('Failed to fetch entries:', error);
        this.error = 'Could not load entries.';
      }
    },

    /**
     * Creates a new diary entry.
     * @param {string} title - The title of the new entry.
     * @param {string} content - The content of the new entry.
     */
    async createEntry(title, content) {
      const authStore = useAuthStore();
      
      // Ensure the user is authenticated before creating an entry.
      if (!authStore.token) {
        this.error = 'User not authenticated.';
        return;
      }

      this.error = null;
      try {
        // Send a POST request to the API with the new entry's data.
        await axios.post('http://localhost:8000/entries/', 
          {
            title: title,
            content: content
          }, 
          {
            headers: {
              'Authorization': `Bearer ${authStore.token}`
            }
          }
        );
        
        // After successful creation, refresh the entries list to show the new entry.
        await this.fetchEntries();

      } catch (error) {
        console.error('Failed to create entry:', error);
        this.error = 'Could not save the new entry.';
      }
    }
  },
});