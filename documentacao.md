Eu quero uma API para um mercado.

Cada produto deve haver as informações:

- Nome (obrigatorio) (variavel: nome)
- Preço (obrigatorio) (variavel: preco)
- Descrição (obrigatorio) (variavel: descricao)
- Marca (obrigatorio) (variavel: marca)

O campo "Nome" deve ser uma variável VARCHAR de até 60 caracteres.

O campo "Preço" deve ser uma variável DECIMAL de até com 5 casas, duas após a vírgula.

O campo "Descrição" deve ser uma variável TEXT.

O campo "Marca" deve ser uma variável do tipo VARCHAR de até 60 caracteres.

---

A API deve administrar os produtos, ou seja, realizar um CRUD:

- Devemos validar o cadastro de produtos
- Devemos permitir a consulta dos produtos
- Devemos permitir a consulta dos produtos pelo Nome, Preço ou Marca
- Devemos permitir a consulta dos produtos por ID
- Devemos validar o processo de atualização de um produto
- Devemos validar a possibilidade de excluir um produto (para confirmar o front deve validar a ação.)
