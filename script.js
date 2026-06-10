const API_URL = 'http://127.0.0.1:5000';

const container = document.getElementById('produtos-container');

let produtos = [];

/* ==========================
   CARREGAR PRODUTOS
========================== */

async function carregarProdutos() {
  try {
    const resposta = await fetch(`${API_URL}/produtos`);

    produtos = await resposta.json();

    renderizar(produtos);
  } catch (erro) {
    console.error(erro);

    alert('Erro ao carregar produtos.');
  }
}

/* ==========================
   RENDERIZAR CARDS
========================== */

function renderizar(lista) {
  container.innerHTML = '';

  lista.forEach((produto) => {
    const card = document.createElement('div');

    card.classList.add('card');

    card.innerHTML = `
            <h2>${produto.nome}</h2>

            <p>
                <strong>Marca:</strong>
                ${produto.marca}
            </p>

            <p>
                ${produto.descricao}
            </p>

            <p class="preco">
                R$ ${Number(produto.preco).toFixed(2)}
            </p>

            <div class="acoes">

                <button
                    class="btn-editar"
                    onclick="editarProduto(${produto.id})">

                    Editar

                </button>

                <button
                    class="btn-excluir"
                    onclick="excluirProduto(${produto.id})">

                    Excluir

                </button>

            </div>
        `;

    container.appendChild(card);
  });
}

/* ==========================
   ABRIR MODAL PARA CADASTRAR
========================== */

function abrirModalCadastro() {
  document.getElementById('modo').value = 'cadastrar';

  document.querySelector('#modal-editar h2').innerText = 'Cadastrar Produto';

  document.getElementById('editar-id').value = '';

  document.getElementById('editar-nome').value = '';

  document.getElementById('editar-marca').value = '';

  document.getElementById('editar-descricao').value = '';

  document.getElementById('editar-preco').value = '';

  document.getElementById('modal-editar').style.display = 'flex';
}

/* ==========================
   ABRIR MODAL PARA EDITAR
========================== */

function editarProduto(id) {
  const produto = produtos.find((p) => p.id === id);

  document.getElementById('modo').value = 'editar';

  document.querySelector('#modal-editar h2').innerText = 'Editar Produto';

  document.getElementById('editar-id').value = produto.id;

  document.getElementById('editar-nome').value = produto.nome;

  document.getElementById('editar-marca').value = produto.marca;

  document.getElementById('editar-descricao').value = produto.descricao;

  document.getElementById('editar-preco').value = produto.preco;

  document.getElementById('modal-editar').style.display = 'flex';
}

/* ==========================
   FECHAR MODAL
========================== */

function fecharModal() {
  document.getElementById('modal-editar').style.display = 'none';
}

/* ==========================
   SALVAR FORMULÁRIO
========================== */

document
  .getElementById('form-editar')
  .addEventListener('submit', async function (e) {
    e.preventDefault();

    const modo = document.getElementById('modo').value;

    const id = document.getElementById('editar-id').value;

    const dados = {
      nome: document.getElementById('editar-nome').value,

      marca: document.getElementById('editar-marca').value,

      descricao: document.getElementById('editar-descricao').value,

      preco: document.getElementById('editar-preco').value,
    };

    try {
      if (modo === 'cadastrar') {
        await fetch(`${API_URL}/produtos`, {
          method: 'POST',

          headers: {
            'Content-Type': 'application/json',
          },

          body: JSON.stringify(dados),
        });

        alert('Produto cadastrado com sucesso!');
      } else {
        await fetch(`${API_URL}/produtos/${id}`, {
          method: 'PUT',

          headers: {
            'Content-Type': 'application/json',
          },

          body: JSON.stringify(dados),
        });

        alert('Produto atualizado com sucesso!');
      }

      fecharModal();

      carregarProdutos();
    } catch (erro) {
      console.error(erro);

      alert('Erro ao salvar produto.');
    }
  });

/* ==========================
   EXCLUIR PRODUTO
========================== */

async function excluirProduto(id) {
  const confirmar = confirm('Deseja realmente excluir este produto?');

  if (!confirmar) {
    return;
  }

  try {
    await fetch(`${API_URL}/produtos/${id}`, {
      method: 'DELETE',
    });

    alert('Produto removido com sucesso!');

    carregarProdutos();
  } catch (erro) {
    console.error(erro);

    alert('Erro ao excluir produto.');
  }
}

/* ==========================
   FECHAR MODAL AO CLICAR FORA
========================== */

window.onclick = function (event) {
  const modal = document.getElementById('modal-editar');

  if (event.target === modal) {
    fecharModal();
  }
};

/* ==========================
   INICIAR SISTEMA
========================== */

carregarProdutos();
