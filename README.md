# 🚀 Atividade Prática 4: API CRUD de Produtos com Flask e SQLite

Este projeto implementa uma API RESTful completa com operações CRUD (Create, Read, Update, Delete) para gerenciar produtos.

O desenvolvimento utiliza o framework **Flask** em Python para as rotas e o **SQLite** como banco de dados.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Flask** (Framework Web)
* **SQLite3** (Banco de dados nativo do Python)
* **Jinja2** (Templates HTML)

---

## 📋 Estrutura do Projeto

O banco de dados e os templates estão organizados nas seguintes pastas:

flask-atividade-04/├── venv/                       # Ambiente virtual (ignorado pelo Git)├── database/│   └── db-produtos.db          # Arquivo do banco de dados SQLite com a tabela 'produtos'├── templates/│   ├── cadastrar.html          # Formulário de criação│   ├── listar.html             # Tabela com listagem, links para Alterar e Excluir│   ├── alterar.html            # Formulário de edição│   └── 404.html                # Página de erro customizada├── app.py                      # Lógica principal da aplicação e rotas CRUD└── requirements.txt            # Dependências Python└── README.md                   # Este arquivo
---

## ⚙️ Configuração e Execução

Siga os passos abaixo para configurar e rodar a aplicação:

### 1. Ambiente Virtual

Abra o Terminal na pasta raiz do projeto (`flask-atividade-04`) e ative o ambiente virtual:

```bash
.\venv\Scripts\activate
2. Instalação das DependênciasInstale todas as bibliotecas necessárias (Flask, etc.):Bashpip install -r requirements.txt
3. Execução da AplicaçãoInicie o servidor Flask:Bashpython app.py
4. AcessoAcesse a aplicação no seu navegador:http://127.0.0.1:5000/🗺️ Endpoints (Rotas)A aplicação implementa as seguintes rotas:Rota (URL)Método RESTFuncionalidade (CRUD)/GETRedireciona para /produtos/listar./produtos/cadastrarGET e POSTCREATE: Exibe o formulário e insere novos produtos./produtos/listarGETREAD: Lista todos os produtos cadastrados./produtos/alterar/<int:id>GET e POSTUPDATE: Carrega os dados para edição e salva./produtos/excluir/<int:id>POSTDELETE: Remove o registro do produto especificado.
---

## 💾 Passo 3: Salvar e Enviar o README

Após colar o conteúdo no `README.md` e salvá-lo (`Ctrl + S`), você precisa enviá-lo ao GitHub.

1.  **Gere o `requirements.txt` (Atualizado):**

    ```bash
    pip freeze > requirements.txt
    ```

2.  **Adicionar e Commit:**

    ```bash
    git add .
    git commit -m "Adiciona README.md e atualiza requirements.txt"
    ```

3.  **Enviar para o GitHub (Push):**

    ```bash
    git push origin main
    ```
