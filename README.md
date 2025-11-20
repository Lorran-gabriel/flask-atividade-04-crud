📄 Código Markdown para o README.mdCopie e cole este texto no arquivo README.md (ou use o editor do GitHub):Markdown# 🚀 Atividade Prática 4: API CRUD de Produtos com Flask e SQLite

Este projeto foi desenvolvido como a **Atividade Prática 4** do curso. O objetivo é demonstrar a implementação de uma API completa, oferecendo todas as funcionalidades de **CRUD** (Criação, Leitura, Atualização e Deleção) para gerenciar um catálogo de produtos.

A solução é construída usando o **framework Flask** em Python para o roteamento e a lógica de negócios, e utiliza o **SQLite** como o sistema de gerenciamento de banco de dados, garantindo persistência e organização dos dados.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Flask** (Framework Web)
* **SQLite3** (Banco de dados nativo do Python)
* **Jinja2** (Templates HTML)

---

## 📋 Estrutura do Projeto

O código está organizado dentro da pasta `flask-atividade-04`.

flask-atividade-04/├── database/│   └── db-produtos.db          # Arquivo do banco de dados SQLite com a tabela 'produtos'├── templates/│   ├── cadastrar.html          # Formulário de criação (CREATE)│   ├── listar.html             # Tabela com listagem (READ)│   ├── alterar.html            # Formulário de edição (UPDATE)│   └── 404.html                # Página de erro customizada└── app.py                      # Lógica principal da aplicação e rotas CRUD
---

## ⚙️ Configuração e Execução

Siga os passos abaixo para configurar e rodar a aplicação:

### 1. Ativação do Ambiente Virtual

Abra o Terminal na pasta raiz do projeto (`flask-atividade-04`) e ative o ambiente virtual:

```bash
.\venv\Scripts\activate
2. Instalação das DependênciasInstale as bibliotecas necessárias:Bashpip install -r requirements.txt
3. Execução da AplicaçãoInicie o servidor Flask:Bashpython app.py
4. Acesso e TesteAcesse a aplicação no seu navegador para testar as rotas CRUD:http://127.0.0.1:5000/🗺️ Endpoints (Rotas)A aplicação implementa as seguintes rotas:Rota (URL)Método RESTFuncionalidade (CRUD)/GETRedireciona para /produtos/listar./produtos/cadastrarGET e POSTCREATE: Exibe o formulário e insere novos produtos./produtos/listarGETREAD: Lista todos os produtos cadastrados./produtos/alterar/<int:id>GET e POSTUPDATE: Carrega os dados para edição e salva./produtos/excluir/<int:id>POSTDELETE: Remove o registro do produto especificado.
---

## 💾 Próximo Passo: Envio Final do README

Se você ainda não enviou este arquivo para o GitHub, siga estes comandos no seu Terminal (na pasta `flask-atividade-04`):

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
