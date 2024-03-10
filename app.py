from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def get_personas():
    
    lista_personas = [
        {'nombre': 'Marlon'},
        {'nombre': 'Camila'},
        {'nombre': 'Keiner'},
        {'nombre': 'Joice'},
        {'nombre': 'Tony'},
    ]
 
    return jsonify(lista_personas)


if __name__ == '__main__':
    app.run(debug=True)
