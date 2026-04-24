# Produto 1: Chatbot para Website

Este é o primeiro produto construído utilizando o **AI Framework Core**. Ele demonstra a integração entre um frontend simples em HTML/TailwindCSS e o backend Flask do framework.

## Funcionalidades

*   Interface de chat responsiva.
*   Integração direta com o `AIEngine` via API.
*   Processamento de linguagem natural em tempo real.

## Como Executar

1.  Certifique-se de que o backend do framework está rodando:
    ```bash
    cd backend
    python app.py
    ```
2.  Abra o arquivo `index.html` no seu navegador.
3.  Interaja com o chatbot.

## Estrutura do Código

*   `index.html`: Interface do usuário e lógica de chamada da API.
*   O backend processa a requisição usando o módulo `core/ai_engine`.
