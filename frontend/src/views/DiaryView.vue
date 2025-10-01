<script setup>
import { onMounted, ref } from 'vue'
import { useDiaryStore } from '@/stores/diary'

// Create an instance of our store.
const diaryStore = useDiaryStore();

// Reactive variables for the new note's title and content.
const newTitle = ref('');
const newContent = ref('');

/**
 * Handles saving a new note.
 */
const handleSaveNote = async () => {
  // Check if the title is not empty.
  if (newTitle.value.trim() === '') {
    alert('Please provide a title for your note.');
    return;
  }

  // Call the store's action, passing the title and content.
  await diaryStore.createEntry(newTitle.value, newContent.value);

  // Clear the editor fields after saving.
  newTitle.value = '';
  newContent.value = '';
};

// Tell Vue to call the fetchEntries() action as soon as the component is mounted.
onMounted(() => {
  diaryStore.fetchEntries();
});
</script>

<template>
  <div class="diary-layout">
    <!-- Left Column: Notes Menu -->
    <aside class="sidebar">
      <div class="sidebar-header">
        <h2>My Notes</h2>
        <button class="new-entry-button">+</button>
      </div>
      <ul class="entry-list">
        <li v-if="diaryStore.entries.length === 0" class="entry-item-empty">
          No entries yet. Click '+' to create one.
        </li>
        <li v-for="entry in diaryStore.entries" :key="entry.id" class="entry-item">
          <h3>{{ entry.title }}</h3>
          <p>{{ entry.content ? entry.content.substring(0, 50) + '...' : '' }}</p>
        </li>
      </ul>
    </aside>

      <!-- Right Column: Text Editor -->
      <main class="main-content">
        <div class="editor-container">
          <input   v-model="newTitle" 
            type="text" 
            class="title-input" 
            placeholder="Give your note a title..." 
          />
          <textarea 
            v-model="newContent" 
            class="content-textarea" 
            placeholder="Start writing here..."
          ></textarea>
        </div>
        <div class="editor-actions">
          <button @click="handleSaveNote" class="save-button">Save Note</button>
        </div>
      </main>
    </div>
  </template>
  
  <style scoped>
  .diary-layout {
    display: flex;
    height: calc(100vh - 65px); /* Full viewport height minus header */
  }
  
  /* --- Sidebar --- */
  .sidebar {
    width: 300px;
    background-color: #f8f9fa;
    border-right: 1px solid #e9ecef;
    display: flex;
    flex-direction: column;
  }
  
  .sidebar-header {
    padding: 1rem;
    border-bottom: 1px solid #e9ecef;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .sidebar-header h2 {
    font-size: 1.2rem;
    color: #303030;
    margin: 0;
  }
  
  .new-entry-button {
    background-color: #076a7e;
    color: white;
    border: none;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    font-size: 1.5rem;
    line-height: 28px;
    cursor: pointer;
  }
  
  .entry-list {
    list-style: none;
    padding: 0;
    margin: 0;
    overflow-y: auto; /* Adds scroll if the list is long */
  }
  
  .entry-item {
    padding: 1rem;
    border-bottom: 1px solid #e9ecef;
    cursor: pointer;
    transition: background-color 0.2s;
  }
  
  .entry-item:hover {
    background-color: #e9ecef;
  }
  
  .entry-item.active {
    background-color: #d1f1f2;
  }
  
  .entry-item h3 {
    margin: 0 0 0.25rem;
    color: #303030;
  }
  
  .entry-item p {
    margin: 0;
    font-size: 0.9rem;
    color: #828282;
  }
  
  /* --- Main Content (Editor) --- */
  .main-content {
    flex-grow: 1; /* Occupies remaining space */
    display: flex;
    flex-direction: column;
    background-color: #ffffff;
  }
  
  .editor-container {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    padding: 2rem;
  }
  
  .title-input, .content-textarea {
    border: none;
    outline: none;
    font-family: inherit;
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
  }
  
  .title-input {
    font-size: 2rem;
    font-weight: bold;
    padding-bottom: 1rem;
    color: #303030;
  }
  
  .content-textarea {
    flex-grow: 1;
    font-size: 1.1rem;
    line-height: 1.6;
    resize: none; /* Prevent user from resizing */
    color: #303030;
  }
  
  .editor-actions {
    padding: 1rem 2rem;
    text-align: right;
    border-top: 1px solid #e9ecef;
  }
  
  .save-button {
    background-color: #076a7e;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
  }
  </style>