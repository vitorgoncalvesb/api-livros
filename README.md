# 📚 API de Livros

Uma API REST desenvolvida em **Python** utilizando **FastAPI** para gerenciamento de livros. O projeto tem como objetivo colocar em prática os principais conceitos relacionados ao desenvolvimento de APIs, comunicação HTTP, operações CRUD, integração com banco de dados e documentação de endpoints.

A aplicação permite trabalhar com um catálogo de livros através de diferentes operações, possibilitando **cadastrar, consultar, atualizar e excluir livros** de maneira estruturada.

O projeto também conta com integração com banco de dados **MySQL/MariaDB**, utilizando **SQLAlchemy** para comunicação com o banco e **Pydantic** para validação e organização dos dados recebidos pela API.

---

## 🚀 Sobre o projeto

A **API de Livros** foi desenvolvida como um projeto para praticar o desenvolvimento de uma aplicação back-end utilizando uma arquitetura baseada em APIs REST.

A ideia principal é disponibilizar um serviço responsável pelo gerenciamento de um catálogo de livros. Por meio dos endpoints disponibilizados pela API, um cliente pode realizar as principais operações necessárias para manipular os registros armazenados no banco de dados.

Entre as operações planejadas estão:

* 🔎 **GET** — Consultar livros
* ➕ **POST** — Cadastrar novos livros
* ✏️ **PUT** — Atualizar livros existentes
* 🗑️ **DELETE** — Excluir livros

Essas operações formam o CRUD da aplicação:

> **C**reate → Criar
> **R**ead → Consultar
> **U**pdate → Atualizar
> **D**elete → Excluir

O projeto também possui uma rota de saúde da aplicação, utilizada para verificar se a API está funcionando corretamente e se a conexão com o banco de dados está disponível.

---

## 🎯 Objetivos

O desenvolvimento desta API tem como principais objetivos:

* Compreender o funcionamento de uma API REST;
* Praticar a criação de endpoints utilizando FastAPI;
* Trabalhar com os métodos HTTP;
* Implementar operações CRUD;
* Integrar uma aplicação Python a um banco de dados relacional;
* Utilizar SQLAlchemy para comunicação com o banco;
* Trabalhar com variáveis de ambiente;
* Validar dados recebidos pela API;
* Utilizar documentação automática de APIs;
* Aprender a testar endpoints utilizando ferramentas como Swagger UI;
* Organizar um projeto back-end de maneira modular e escalável.

---

## 🛠️ Tecnologias utilizadas

### Python

A linguagem principal utilizada no desenvolvimento do projeto.

### FastAPI

Framework utilizado para construção da API REST.

O FastAPI permite criar endpoints de maneira simples e possui recursos integrados para validação de dados e geração automática da documentação da API.

### SQLAlchemy

Biblioteca utilizada para realizar a comunicação entre a aplicação Python e o banco de dados.

Ela permite trabalhar com o banco de maneira mais organizada, utilizando recursos de ORM e abstraindo boa parte das operações diretamente em SQL.

### Pydantic

Utilizado para validação e estruturação dos dados recebidos pela API.

Isso ajuda a garantir que as informações enviadas nas requisições estejam no formato esperado pela aplicação.

### PyMySQL

Driver utilizado para realizar a comunicação entre o SQLAlchemy e o banco de dados MySQL/MariaDB.

### Uvicorn

Servidor ASGI utilizado para executar a aplicação FastAPI.

### MySQL / MariaDB

Banco de dados relacional utilizado para armazenar as informações da aplicação.

---

## 🧩 Arquitetura do projeto

A estrutura atual do repositório está organizada da seguinte maneira:

```text
api-livros/
│
├── app/
│   ├── __init__.py
│   ├── database.py
│   └── main.py
│
├── database/
│   └── biblioteca_db.sql
│
├── .gitignore
├── README.md
└── requirements.txt
```

### 📁 `app/`

Contém os principais arquivos responsáveis pelo funcionamento da aplicação.

#### `main.py`

Arquivo responsável pela inicialização da aplicação FastAPI e definição das rotas.

É neste arquivo que a aplicação é criada e onde ficam os endpoints disponibilizados pela API.

#### `database.py`

Responsável pelas configurações relacionadas ao banco de dados.

O arquivo utiliza variáveis de ambiente para obter informações como:

* Usuário do banco;
* Senha;
* Host;
* Porta;
* Nome do banco.

A aplicação utiliza SQLAlchemy para criar a conexão com o banco de dados.

### 📁 `database/`

Diretório destinado aos arquivos relacionados à estrutura do banco.

#### `biblioteca_db.sql`

Arquivo SQL utilizado para criação do banco de dados da aplicação.

O banco utilizado pelo projeto é chamado:

```text
biblioteca_db
```

### 📄 `requirements.txt`

Arquivo que contém as dependências necessárias para executar o projeto.

---

# 🔌 Endpoints

A API utiliza os métodos HTTP tradicionais para realizar as operações sobre os livros.

## 🔎 GET — Consultar livros

O método `GET` é utilizado para recuperar informações.

### Buscar todos os livros

```http
GET /livros
```

Esse endpoint retorna a lista de livros cadastrados no banco de dados.

### Exemplo de resposta

```json
[
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "ano_publicacao": 1899
    },
    {
        "id": 2,
        "titulo": "O Hobbit",
        "autor": "J. R. R. Tolkien",
        "ano_publicacao": 1937
    }
]
```

---

## 🔎 GET — Buscar um livro específico

Também é possível consultar um único livro utilizando seu identificador.

```http
GET /livros/{id}
```

### Exemplo

```http
GET /livros/1
```

### Exemplo de resposta

```json
{
    "id": 1,
    "titulo": "Dom Casmurro",
    "autor": "Machado de Assis",
    "ano_publicacao": 1899
}
```

Caso o livro solicitado não exista, a API deverá retornar um código HTTP apropriado, como:

```http
404 Not Found
```

---

# ➕ POST — Cadastrar um livro

O método `POST` é utilizado para criar um novo registro.

```http
POST /livros
```

Os dados do novo livro devem ser enviados no corpo da requisição.

### Exemplo de requisição

```json
{
    "titulo": "O Pequeno Príncipe",
    "autor": "Antoine de Saint-Exupéry",
    "ano_publicacao": 1943
}
```

### Exemplo de resposta

```json
{
    "id": 3,
    "titulo": "O Pequeno Príncipe",
    "autor": "Antoine de Saint-Exupéry",
    "ano_publicacao": 1943
}
```

O `POST` é utilizado sempre que o objetivo for **criar um novo recurso**.

---

# ✏️ PUT — Atualizar um livro

O método `PUT` é utilizado para atualizar informações de um livro já existente.

```http
PUT /livros/{id}
```

### Exemplo

```http
PUT /livros/3
```

### Corpo da requisição

```json
{
    "titulo": "O Pequeno Príncipe",
    "autor": "Antoine de Saint-Exupéry",
    "ano_publicacao": 1943
}
```

A API deverá localizar o livro pelo seu `id` e atualizar suas informações.

### Exemplo de resposta

```json
{
    "id": 3,
    "titulo": "O Pequeno Príncipe",
    "autor": "Antoine de Saint-Exupéry",
    "ano_publicacao": 1943
}
```

---

# 🗑️ DELETE — Excluir um livro

O método `DELETE` é utilizado para remover um livro do banco de dados.

```http
DELETE /livros/{id}
```

### Exemplo

```http
DELETE /livros/3
```

Após a execução da operação, o livro correspondente ao identificador informado será removido.

Uma resposta possível para uma exclusão realizada com sucesso é:

```http
204 No Content
```

---

# ❤️ Health Check

Além das operações relacionadas aos livros, a aplicação possui um endpoint responsável por verificar a saúde da API e sua conexão com o banco de dados.

```http
GET /health
```

Esse endpoint executa uma consulta simples no banco para verificar se a conexão está funcionando corretamente.

### Resposta esperada

```json
{
    "status": "ok",
    "database": "connected"
}
```

Essa rota é especialmente útil durante o desenvolvimento para identificar rapidamente problemas relacionados à conexão com o banco de dados.

---

# 📊 Resumo dos endpoints

| Método   | Endpoint       | Descrição                                  |
| -------- | -------------- | ------------------------------------------ |
| `GET`    | `/livros`      | Lista todos os livros                      |
| `GET`    | `/livros/{id}` | Busca um livro específico                  |
| `POST`   | `/livros`      | Cadastra um novo livro                     |
| `PUT`    | `/livros/{id}` | Atualiza um livro                          |
| `DELETE` | `/livros/{id}` | Remove um livro                            |
| `GET`    | `/health`      | Verifica o funcionamento da API e do banco |

> **Observação:** os endpoints acima representam a estrutura CRUD planejada para o gerenciamento de livros. Conforme o desenvolvimento do projeto avançar, os campos, respostas e regras de negócio podem ser ajustados.

---

# 📋 Códigos HTTP

A API utiliza códigos de status HTTP para indicar o resultado das operações.

| Código | Significado           | Utilização                         |
| ------ | --------------------- | ---------------------------------- |
| `200`  | OK                    | Requisição realizada com sucesso   |
| `201`  | Created               | Novo livro criado com sucesso      |
| `204`  | No Content            | Livro excluído com sucesso         |
| `400`  | Bad Request           | Dados enviados de maneira inválida |
| `404`  | Not Found             | Livro não encontrado               |
| `422`  | Unprocessable Entity  | Dados não passaram na validação    |
| `500`  | Internal Server Error | Erro interno da aplicação          |

---

# 🗄️ Banco de dados

O projeto utiliza um banco de dados relacional chamado:

```text
biblioteca_db
```

A conexão com o banco é realizada utilizando:

```text
SQLAlchemy
      ↓
PyMySQL
      ↓
MySQL / MariaDB
```

As informações de conexão não devem ser inseridas diretamente no código-fonte.

Em vez disso, o projeto utiliza variáveis de ambiente através de um arquivo `.env`.

### Exemplo de configuração

```env
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=3306
DB_NAME=biblioteca_db
```

> ⚠️ **Importante:** o arquivo `.env` não deve ser enviado para o GitHub, principalmente quando contém senhas ou outras informações sensíveis.

---

# ⚙️ Instalação

Para executar o projeto localmente, é necessário ter instalado:

* Python 3.10 ou superior;
* MySQL ou MariaDB;
* Git;
* Pip.

---

## 1. Clonar o repositório

```bash
git clone https://github.com/vitorgoncalvesb/api-livros.git
```

Entre na pasta do projeto:

```bash
cd api-livros
```

---

## 2. Criar um ambiente virtual

É recomendado utilizar um ambiente virtual para manter as dependências do projeto isoladas.

No Windows:

```bash
python -m venv venv
```

Depois, ative o ambiente:

```bash
venv\Scripts\activate
```

No Linux ou macOS:

```bash
python3 -m venv venv
```

Ativação:

```bash
source venv/bin/activate
```

---

## 3. Instalar as dependências

Com o ambiente virtual ativado:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` contém as principais dependências utilizadas pela aplicação, incluindo FastAPI, SQLAlchemy, PyMySQL, Pydantic e Uvicorn.

---

# 🗄️ Configurando o banco de dados

Antes de executar a API, é necessário possuir uma instância do MySQL/MariaDB funcionando.

O projeto disponibiliza um script SQL dentro da pasta:

```text
database/biblioteca_db.sql
```

Esse arquivo pode ser utilizado para criar a estrutura inicial do banco.

O banco esperado pela aplicação é:

```text
biblioteca_db
```

Depois de criar o banco, configure as credenciais no arquivo `.env`.

Exemplo:

```env
DB_USER=root
DB_PASSWORD=senha
DB_HOST=localhost
DB_PORT=3306
DB_NAME=biblioteca_db
```

As informações devem ser adaptadas de acordo com a configuração do ambiente local.

---

# ▶️ Executando a API

Com o ambiente virtual ativado e as dependências instaladas, execute:

```bash
uvicorn app.main:app --reload
```

A opção `--reload` faz com que o servidor seja reiniciado automaticamente quando alterações forem detectadas durante o desenvolvimento.

Por padrão, a aplicação ficará disponível em:

```text
http://127.0.0.1:8000
```

---

# 📖 Documentação da API

Uma das principais vantagens do FastAPI é a geração automática da documentação dos endpoints.

Depois de iniciar a aplicação, acesse:

```text
http://127.0.0.1:8000/docs
```

Nessa página é possível visualizar e testar os endpoints através do **Swagger UI**.

A documentação permite:

* Visualizar todos os endpoints;
* Ver os métodos HTTP disponíveis;
* Conferir os parâmetros necessários;
* Visualizar os modelos de dados;
* Enviar requisições diretamente pelo navegador;
* Analisar as respostas da API;
* Testar diferentes códigos de resposta.

Também é possível acessar a documentação alternativa do FastAPI em:

```text
http://127.0.0.1:8000/redoc
```

---

# 🧪 Testando a API

Uma das formas mais simples de testar a aplicação é utilizando o Swagger UI.

Com o servidor em execução:

```text
http://127.0.0.1:8000/docs
```

Escolha um endpoint, clique em **Try it out**, preencha os dados necessários e execute a requisição.

Por exemplo, para cadastrar um livro:

```http
POST /livros
```

Podemos enviar:

```json
{
    "titulo": "1984",
    "autor": "George Orwell",
    "ano_publicacao": 1949
}
```

Depois disso, podemos utilizar:

```http
GET /livros
```

para verificar se o livro foi armazenado corretamente.

Também podemos testar:

```http
PUT /livros/{id}
```

para modificar seus dados e:

```http
DELETE /livros/{id}
```

para removê-lo.

Dessa maneira, é possível testar todo o ciclo CRUD da aplicação.

---

# 🔄 Funcionamento da aplicação

De maneira simplificada, o fluxo da aplicação funciona da seguinte forma:

```text
                 CLIENTE
                    │
                    ▼
             ┌─────────────┐
             │   FastAPI   │
             └──────┬──────┘
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
      Validação            Rotas
      Pydantic             HTTP
          │                   │
          └─────────┬─────────┘
                    │
                    ▼
               SQLAlchemy
                    │
                    ▼
               PyMySQL
                    │
                    ▼
             MySQL / MariaDB
                    │
                    ▼
              biblioteca_db
```

O cliente envia uma requisição HTTP para a API.

A aplicação recebe essa requisição através de um endpoint definido no FastAPI. Os dados recebidos são validados e processados antes que a operação seja realizada.

Quando a operação envolve o banco de dados, a aplicação utiliza o SQLAlchemy para realizar a comunicação com o banco através do PyMySQL.

Após a operação, a API retorna uma resposta HTTP contendo o resultado para o cliente.

---

# 🧱 Conceito CRUD

O projeto foi estruturado em torno das quatro operações fundamentais de manipulação de dados.

### Create

Representado pelo método:

```http
POST
```

Responsável por criar novos livros.

### Read

Representado pelo método:

```http
GET
```

Responsável por consultar os livros cadastrados.

### Update

Representado pelo método:

```http
PUT
```

Responsável por atualizar livros existentes.

### Delete

Representado pelo método:

```http
DELETE
```

Responsável por remover livros.

Dessa maneira:

```text
             API DE LIVROS

        ┌─────────────────────┐
        │       CREATE        │
        │       POST          │
        └─────────────────────┘

        ┌─────────────────────┐
        │        READ         │
        │        GET          │
        └─────────────────────┘

        ┌─────────────────────┐
        │       UPDATE        │
        │        PUT          │
        └─────────────────────┘

        ┌─────────────────────┐
        │       DELETE        │
        │       DELETE        │
        └─────────────────────┘
```

---

# 🔐 Boas práticas

Durante o desenvolvimento da aplicação, algumas boas práticas devem ser consideradas:

### Variáveis de ambiente

Credenciais e configurações do banco devem ser armazenadas em variáveis de ambiente, evitando que informações sensíveis sejam expostas no código.

### Validação

Os dados recebidos pelos endpoints devem ser validados antes de serem utilizados pela aplicação.

### Status HTTP

Cada operação deve retornar códigos HTTP adequados para representar o resultado da requisição.

### Separação de responsabilidades

A estrutura do projeto deve ser organizada de maneira que cada arquivo e módulo tenha uma responsabilidade bem definida.

### Documentação

Os endpoints devem ser documentados para facilitar sua utilização e manutenção.

---

# 📈 Possíveis melhorias futuras

O projeto pode ser expandido futuramente com diversas funcionalidades.

Algumas possibilidades incluem:

* [ ] Implementação completa do CRUD de livros;
* [ ] Criação dos modelos do banco utilizando SQLAlchemy;
* [ ] Criação dos schemas utilizando Pydantic;
* [ ] Implementação de tratamento de erros;
* [ ] Paginação da lista de livros;
* [ ] Pesquisa de livros por título;
* [ ] Pesquisa por autor;
* [ ] Filtros por ano de publicação;
* [ ] Ordenação dos resultados;
* [ ] Sistema de autenticação;
* [ ] Controle de usuários;
* [ ] Testes automatizados;
* [ ] Dockerização da aplicação;
* [ ] Deploy da API;
* [ ] Integração com ferramentas de monitoramento;
* [ ] Versionamento da API, como `/api/v1`;
* [ ] Melhorias na documentação dos endpoints.

---

# 🎓 Finalidade acadêmica

Este projeto possui caráter principalmente **didático e educacional**, sendo utilizado para colocar em prática conhecimentos relacionados ao desenvolvimento back-end e à construção de APIs.

Por meio dele, são trabalhados conceitos importantes para o desenvolvimento de aplicações modernas, como:

* APIs REST;
* HTTP;
* CRUD;
* FastAPI;
* Python;
* Banco de dados relacionais;
* SQL;
* SQLAlchemy;
* Validação de dados;
* Documentação de APIs;
* Variáveis de ambiente;
* Arquitetura de aplicações back-end.

A proposta é transformar conceitos teóricos em uma aplicação funcional, permitindo compreender na prática como uma API recebe requisições, processa informações, interage com um banco de dados e devolve respostas para seus clientes.

---

# 👨‍💻 Autor

Desenvolvido por **Vitor Gonçalves Barros**.

GitHub:

**[@vitorgoncalvesb](https://github.com/vitorgoncalvesb)**

Repositório:

**[api-livros](https://github.com/vitorgoncalvesb/api-livros)**

---

# 📄 Licença

Este projeto foi desenvolvido para fins educacionais.

Caso o projeto seja posteriormente disponibilizado sob uma licença específica, esta seção poderá ser atualizada de acordo com os termos escolhidos.

---

## ⭐ Considerações finais

A **API de Livros** representa uma aplicação back-end simples, porém construída sobre conceitos fundamentais para o desenvolvimento de sistemas modernos.

A partir de uma estrutura baseada em **FastAPI**, **Python** e **MySQL/MariaDB**, o projeto busca demonstrar todo o fluxo de uma API REST, desde o recebimento de uma requisição HTTP até a comunicação com o banco de dados e o retorno de uma resposta ao cliente.

O principal foco está na implementação das quatro operações fundamentais do CRUD — **Create, Read, Update e Delete** — permitindo que o catálogo de livros seja criado e manipulado através de endpoints bem definidos.

Além de servir como aplicação funcional, o projeto também funciona como uma base para futuras evoluções, podendo receber autenticação, testes automatizados, filtros, paginação, novas entidades e outras funcionalidades comuns em sistemas back-end.

**📚 Aprender APIs é entender como diferentes aplicações conseguem conversar entre si. Este projeto é um passo nessa direção.**
