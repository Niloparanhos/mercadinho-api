# Mercadinho — API de Cadastro de Produtos

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white)

Aplicação web para gerenciamento de produtos de um mercado de pequeno porte. O back-end foi desenvolvido do zero com Flask e MySQL, incluindo uma API REST completa. O front-end consome a API via fetch e permite realizar todas as operações sem sair da página.

## Funcionalidades

- Listagem de todos os produtos em cards
- Cadastro de novos produtos via modal
- Edição de produtos existentes
- Exclusão com confirmação
- Validação de campos obrigatórios no back-end

## Tecnologias utilizadas

- **Back-end:** Python + Flask + Flask-CORS
- **Banco de dados:** MySQL
- **Front-end:** HTML, CSS e JavaScript (vanilla)

## Estrutura do projeto

```
mercadinho/
├── main.py           # API Flask
├── index.html        # Interface web
├── script.js         # Lógica do front-end
├── styles.css        # Estilos
├── requirements.txt  # Dependências Python
├── .env.example      # Modelo de variáveis de ambiente
└── .gitignore
```

## Como rodar localmente

1. Clone o repositório:
```bash
git clone https://github.com/niloparanhos/mercadinho-api.git
cd mercadinho-api
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o .env com suas credenciais do MySQL
```

4. Crie o banco de dados no MySQL:
```sql
CREATE DATABASE mercadinho;

USE mercadinho;

CREATE TABLE produtos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(60) NOT NULL,
  marca VARCHAR(60) NOT NULL,
  descricao TEXT NOT NULL,
  preco DECIMAL(7,2) NOT NULL
);
```

5. Rode a API:
```bash
python main.py
```

6. Abra o `index.html` no navegador.

## Endpoints da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /produtos | Lista todos os produtos |
| POST | /produtos | Cadastra um novo produto |
| PUT | /produtos/<id> | Atualiza um produto |
| DELETE | /produtos/<id> | Remove um produto |

## Aprendizados

Projeto desenvolvido para praticar a construção de uma API REST com Flask, modelagem de banco de dados relacional com MySQL, integração front-end via fetch API e boas práticas como uso de variáveis de ambiente para proteger credenciais.
