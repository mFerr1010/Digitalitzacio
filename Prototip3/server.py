from flask import Flask, jsonify, request
import dadesserver as dades
import uuid

app = Flask(__name__)

# DAOs
class UserDAO:
    def __init__(self):
        self.users = dades.users

    def get_all_users(self):
        return [user.__dict__ for user in self.users]

    def get_user_by_username_and_password(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user.__dict__
        return None

class ChildDAO:
    def __init__(self):
        self.children = dades.children

    def get_all_children(self):
        return [child.__dict__ for child in self.children]

    def get_children_by_user_id(self, user_id):
        child_ids = [rel["child_id"] for rel in dades.relation_user_child if rel["user_id"] == user_id]
        return [child.__dict__ for child in self.children if child.id in child_ids]

# Crear instancias de los DAOs
user_dao = UserDAO()
child_dao = ChildDAO()

# Tokens activos
active_tokens = {}

# Rutas de la API
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Falten paràmetres'}), 400

    user = user_dao.get_user_by_username_and_password(data['username'], data['password'])
    if user:
        token = str(uuid.uuid4())  # Generar un token único
        active_tokens[token] = user['id']  # Asociar el token con el ID del usuario
        return jsonify({'token': token, 'user': user})  # Incluir los datos del usuario
    else:
        return jsonify({'error': 'Credenciales incorrectas'}), 401

@app.route('/sumar', methods=['POST'])
def sumar():
    # Verificar el token
    token = request.headers.get('Authorization')
    if not token or token not in active_tokens:
        return jsonify({'error': 'Accés no autoritzat'}), 401

    # Obtenir dades JSON
    data = request.json
    if not data or 'num1' not in data or 'num2' not in data:
        return jsonify({'error': 'Falten paràmetres'}), 400

    # Realitzar la suma
    try:
        resultat = data['num1'] + data['num2']
    except TypeError:
        return jsonify({'error': 'Els paràmetres han de ser números'}), 400

    return jsonify({'resultat': resultat})

if __name__ == '__main__':
    app.run(debug=True)