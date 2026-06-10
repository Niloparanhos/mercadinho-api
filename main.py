import mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)


def get_conn():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )


@app.route('/')
def home():
    return 'API de mercado está funcionando.'


@app.route('/produtos', methods=["GET"])
def listar():
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    lista_produtos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(lista_produtos)


@app.route("/produtos", methods=['POST'])
def cadastrar():
    infos_front = request.get_json()
    nome = infos_front.get("nome")
    marca = infos_front.get("marca")
    descricao = infos_front.get("descricao")
    preco = infos_front.get("preco")

    if not nome or not marca or not descricao or not preco:
        return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400

    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    consulta = """
        INSERT INTO produtos (nome, marca, descricao, preco)
        VALUES (%s, %s, %s, %s)
    """
    itens = (nome, marca, descricao, preco)
    cursor.execute(consulta, itens)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensagem': 'Produto cadastrado com sucesso'}), 201


@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar(id):
    infos_front = request.get_json()
    nome = infos_front.get("nome")
    marca = infos_front.get("marca")
    descricao = infos_front.get("descricao")
    preco = infos_front.get("preco")

    if not nome or not marca or not descricao or not preco:
        return jsonify({'erro': 'Todos os campos são obrigatórios'}), 400

    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    consulta = """
        UPDATE produtos
        SET nome = %s, marca = %s, descricao = %s, preco = %s
        WHERE id = %s
    """
    itens = (nome, marca, descricao, preco, id)
    cursor.execute(consulta,itens)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensagem': 'Produto alterado com sucesso'}), 200


@app.route("/produtos/<int:id>", methods=["DELETE"])
def deletar(id):
    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM produtos WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'mensagem': 'Produto deletado com sucesso.'})


if __name__ == '__main__':
    app.run(debug=True)
