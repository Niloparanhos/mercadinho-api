import mysql.connector
from flask import Flask, jsonify, request
from flask_cors import CORS 

conn = mysql.connector.connect(
host = 'localhost',
user = 'root',
password = '3581321Nilo#',
database = 'mercadinho'
)

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
  return 'API de mercado está funcionando.'

@app.route('/produtos', methods=["GET"])
def listar():
  cursor =  conn.cursor(dictionary=True)
  cursor.execute("SELECT * FROM produtos")
  lista_produtos = cursor.fetchall()
  cursor.close()
  return jsonify(lista_produtos)

@app.route("/produtos", methods=['POST'])
def cadastrar():
  infos_front = request.get_json()
  nome = infos_front.get("nome")
  marca = infos_front.get("marca")
  descricao = infos_front.get("descricao")
  preco = infos_front.get("preco")
  cursor = conn.cursor(dictionary=True)
  consulta = f"""
INSERT INTO produtos (nome,marca,descricao,preco) VALUES
(%s,%s,%s, %s)
"""
  itens = (nome,marca,descricao,preco)
  cursor.execute(consulta,itens)
  conn.commit()
  cursor.close()
  return jsonify({'mensagem': 'Produto cadastrado com sucesso'}), 201

@app.route("/produto/<int:id>", methods=["PUT"])
def atualizar(id):
  infos_front = request.get_json()
  nome = infos_front.get("nome")
  marca = infos_front.get("marca")
  descricao = infos_front.get("descricao")
  preco = infos_front.get("preco")
  cursor = conn.cursor(dictionary=True)
  consulta = f"""UPDATE produtos 
                SET
                  nome = %s,
                  marca = %s,
                  descricao = %s,
                  preco = %s
                    WHERE id = %s
                    """
  itens = (nome,marca,descricao,preco,id)
  cursor.execute(consulta,itens)
  conn.commit()
  cursor.close()
  return jsonify({'mensagem'  : 'Produto alterado com sucesso'}), 201

@app.route("/produtos/<int:id>", methods=["DELETE"])
def deletar(id):
  cursor = conn.cursor(dictionary=True)
  consulta = f"DELETE FROM produtos WHERE id = %s"
  itens = (id,)
  cursor.execute(consulta, itens)
  conn.commit()
  cursor.close()
  return jsonify({'mensagem': 'Produto deletado com sucesso.'})



if __name__ == '__main__':
  app.run(debug=True)