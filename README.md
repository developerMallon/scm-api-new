# SCM API - Backend

Este é o backend da aplicação SCM, desenvolvido com **FastAPI** e seguindo uma arquitetura modular para garantir escalabilidade e fácil manutenção.

## 🚀 Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e de alta performance.
- **SQLAlchemy 2.0 (Async)**: ORM para interação com o banco de dados.
- **PostgreSQL**: Banco de dados relacional (via `asyncpg`).
- **Pydantic V2**: Validação de dados e configurações.
- **Alembic**: Gerenciamento de migrações de banco de dados.
- **JWT & Passlib**: Segurança, autenticação e hashing de senhas.

## 📁 Estrutura do Projeto

O projeto utiliza uma arquitetura baseada em módulos dentro da pasta `apps/`, facilitando a separação de responsabilidades:

```text
.
├── apps/               # Módulos da aplicação (Vertical Slices)
│   ├── user/           # Módulo de Usuários
│   │   ├── models/     # Modelos SQLAlchemy
│   │   ├── repositories/ # Lógica de acesso a dados
│   │   ├── routes/     # Definição dos Endpoints
│   │   └── schemas/    # Schemas Pydantic (DTOs)
│   └── api_router.py   # Centralizador de rotas (Router Global)
├── core/               # Configurações centrais (DB, Config, Segurança)
├── main.py             # Ponto de entrada da aplicação
└── requirements.txt    # Dependências do projeto
```

## 🛠️ O que foi feito até agora

1.  **Configuração Base**: Setup inicial do FastAPI com Uvicorn.
2.  **Arquitetura Modular**: Implementação da estrutura de pastas separada por domínios (`apps/`).
3.  **Conexão com Banco de Dados**: Configuração do SQLAlchemy Assíncrono e injeção de dependência para sessões de banco no `core/database.py`.
4.  **Gerenciamento de Rotas**: Centralização das rotas no `apps/api_router.py`. O `main.py` agora importa apenas este router global, mantendo o código limpo.
5.  **Módulo de Usuário**: Estruturação inicial do módulo de usuários incluindo rotas, modelos e schemas.
6.  **Segurança**: Preparação do ambiente para autenticação JWT e criptografia de senhas com `passlib`.

## ⚙️ Como executar

1.  Crie um ambiente virtual:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/Mac
    .\.venv\Scripts\activate   # Windows
    ```

2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3.  Configure o arquivo `.env` com suas credenciais.

4.  Inicie o servidor:
    ```bash
    python main.py
    ```
    Ou via terminal:
    ```bash
    uvicorn main:app --reload
    ```

---
*Documentação em constante atualização.*
