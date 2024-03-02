from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/personas', methods=['GET'])
def index():
    lista_personas = [
        {'name': 'Marlon Rodriguez ariza'},
        {'name': 'Maria Camila Velez'},
        {'name': 'Joice Milena Ariza'},
        {'name': 'Keiner Adrian Rodriguez'},
        {'name': 'Frank De Jesus Ariza'},
    ]
    return jsonify(lista_personas)
if __name__ == '__main__':
    app.run(debug=True)