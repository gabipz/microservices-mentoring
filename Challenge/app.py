from flask import Flask, jsonify, request

app = Flask(__name__)

propose = []

@app.route('/')
def home():
    return "Oi cliente, bem vindo ao sistema de propostas!"

@app.route('/propostas', methods=['GET'])
def get_propostas():
    return jsonify(propose), 200

@app.route('/propostas', methods=['POST'])
def create_proposta():
    propose_data = request.get_json()
    propose_id = len(propose) + 1

    # Lógica para determinar o status
    valor = propose_data['valor']
    if valor < 0:
        return jsonify({'error': 'O valor não pode ser negativo'}), 400
    elif valor <= 10000:
        status = 'Aprovada'
    elif valor > 50000:
        status = 'Recusada'
    else:
        status = 'Em análise'

    proposta = {
        'id': propose_id,
        'nome': propose_data['nome'],
        'valor': valor,
        'status': status
    }
    propose.append(proposta)
    return jsonify(proposta), 201

@app.route('/propostas/<int:proposta_id>', methods=['GET'])
def get_proposta(proposta_id):
    proposta = next((p for p in propose if p['id'] == proposta_id), None)
    if proposta is None:
        return jsonify({'error': 'Proposta não encontrada'}), 404
    return jsonify(proposta), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
