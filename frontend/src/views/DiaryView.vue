<template>
    <div class="diary-layout">
      <!-- Coluna da Esquerda: Menu de Anotações -->
      <aside class="sidebar">
        <div class="sidebar-header">
          <h2>Minhas Anotações</h2>
          <button class="new-entry-button">+</button>
        </div>
        <ul class="entry-list">
          <!-- Placeholder: Anotações serão listadas aqui -->
          <li class="entry-item">
            <h3>Título da Anotação 1</h3>
            <p>Um breve resumo do texto...</p>
          </li>
          <li class="entry-item active">
            <h3>Anotação Ativa</h3>
            <p>Esta é a anotação que está...</p>
          </li>
        </ul>
      </aside>
  
      <!-- Coluna da Direita: Editor de Texto -->
      <main class="main-content">
        <div class="editor-container">
          <input type="text" class="title-input" placeholder="Dê um título à sua anotação..." />
          <textarea class="content-textarea" placeholder="Comece a escrever aqui..."></textarea>
        </div>
        <div class="editor-actions">
          <button class="save-button">Guardar Anotação</button>
        </div>
      </main>
    </div>
  </template>
  
  <style scoped>
  .diary-layout {
    display: flex;
    height: calc(100vh - 65px); /* Altura total da tela menos o header */
  }
  
  /* --- Barra Lateral (Sidebar) --- */
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
    overflow-y: auto; /* Adiciona scroll se a lista for longa */
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
  
  /* --- Conteúdo Principal (Editor) --- */
  .main-content {
    flex-grow: 1; /* Ocupa todo o espaço restante */
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
    resize: none; /* Impede que o usuário redimensione */
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