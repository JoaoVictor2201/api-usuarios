# 👤 API de Usuários

Bem-vindo à **API de Usuários**, um projeto simples e eficiente desenvolvido com **Flask** para gerenciamento de usuários.

Esta API permite operações CRUD (Criar, Ler, Atualizar, Deletar) em uma lista de usuários armazenada em memória. Ideal para estudos e testes rápidos de integração.

## 🚀 Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## 🔧 Instalação e Execução

Siga os passos abaixo para rodar o projeto localmente:

1.  **Clone o repositório** (se estiver usando git):
    ```bash
    git clone https://github.com/seu-usuario/seu-repo.git
    cd seu-repo
    ```

2.  **Crie um ambiente virtual** (recomendado):
    ```powershell
    # Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Instale as dependências**:
    ```bash
    pip install Flask
    ```

4.  **Execute a aplicação**:
    ```bash
    python app.py
    ```
    A API estará rodando em: `http://127.0.0.1:5000`

## 🔌 Endpoints da API

Abaixo estão listadas as rotas disponíveis para interagir com a API.

### 1. Listar todos os usuários
- **Rota:** `/users`
- **Método:** `GET`
- **Descrição:** Retorna uma lista com todos os usuários cadastrados.
- **Resposta Sucesso (200):**
  ```json
  [
    {
      "nome": "João",
      "email": "joao@email.com",
      "cpf": "12345678901",
      "senha": "123"
    }
  ]
  ```

### 2. Buscar usuário por CPF
- **Rota:** `/users/<cpf>`
- **Método:** `GET`
- **Descrição:** Retorna os detalhes de um usuário específico.
- **Resposta Sucesso (200):**
  ```json
  {
    "nome": "João",
    "email": "joao@email.com",
    "cpf": "12345678901",
    "senha": "123"
  }
  ```
- **Resposta Erro (404):** `{"error": "Usuário não encontrado"}`

### 3. Criar novo usuário
- **Rota:** `/users/`
- **Método:** `POST`
- **Body (JSON):**
  ```json
  {
      "nome": "Maria",
      "email": "maria@email.com",
      "senha": "securePass",
      "cpf": "98765432100"
  }
  ```
- **Resposta Sucesso (201):** Retorna o usuário criado.
- **Resposta Erro (400):** `{"error": "Usuário já existe"}` ou `{"error": "Dados inválidos"}`

### 4. Deletar usuário
- **Rota:** `/users/<cpf>`
- **Método:** `DELETE`
- **Descrição:** Remove um usuário do sistema.
- **Resposta Sucesso (200):** `{"message": "Usuário deletado com sucesso"}`
- **Resposta Erro (404):** `{"error": "Usuário não encontrado"}`

## 📁 Estrutura do Projeto

A organização do código segue o padrão **MVC (Model-View-Controller)** adaptado para uma API:

```
.
├── controllers/
│   └── user_controller.py  # Gerencia as rotas e requisições HTTP
├── models/
│   └── user_model.py       # Define a estrutura de dados do Usuário
├── services/
│   └── user_service.py     # Contém a regra de negócios (CRUD)
├── app.py                  # Ponto de entrada da aplicação
└── README.md               # Documentação do projeto
```

## ⚠️ Observações
- Os dados são armazenados **em memória** (lista Python). Se a aplicação for reiniciada, todos os dados serão perdidos.
- Este projeto é para fins educacionais e **não** deve ser usado em produção sem adicionar persistência (banco de dados) e autenticação.

---
### Integrantes do Projeto
- João Victor França - 2402779
- Gustavo Bomfim - 2403139
- Ana Laura Brandão - 2402680
- Alex Manoel - 1701381
- Gabriel Gonçalves - 2402912