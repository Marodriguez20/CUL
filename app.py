from flask import Flask,request,jsonify
import pymysql.cursors
import pymysql

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

connection = pymysql.Connection(
                                   host='localhost',
                                   user= 'root',
                                   port='3307',
                                   password='',
                                   db = 'bdpythonapi' ,
                                   cursorclass=pymysql.cursors.DictCursor)

     

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
     with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
     return jsonify(usuarios)

@app.route('/Usuario', methods=['POST'])
def create_usuario():
    data = request.get_json()
    connection = ()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO Usuario (nombre, email) VALUES (%s, %s)"
            cursor.execute(sql, (data['nombre'],data['email']))
        connection.commit()
            
    return jsonify({'message': 'creacion exitosa'}), 201

@app.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    nombre = request.json['nombre']
    email = request.json['email']
    with connection.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET nombre = %s, email = %s WHERE id = %s", (nombre, email, usuario_id))
        connection.commit()
    return jsonify({"message": "Usuario actualizado correctamente"})

@app.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
        connection.commit()
    return jsonify({"message": "Usuario eliminado correctamente"})

if __name__ == '__main__':
    app.run(debug=True)