from flask import Flask, jsonify, request
import dadesserver as dades

app = Flask(__name__)

# DAOs
class UserDAO:
    def __init__(self):
        self.users = dades.users

    def get_all_users(self):
        return [user.__dict__ for user in self.users]

    def get_user_by_username(self, username):
        for user in self.users:
            if user.username == username:
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

# Rutas de la API
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(user_dao.get_all_users())

@app.route('/users/<string:username>', methods=['GET'])
def get_user_by_username(username):
    user = user_dao.get_user_by_username(username)
    return jsonify(user) if user else ('User not found', 404)

@app.route('/children', methods=['GET'])
def get_children():
    return jsonify(child_dao.get_all_children())

@app.route('/children/<int:user_id>', methods=['GET'])
def get_children_by_user(user_id):
    return jsonify(child_dao.get_children_by_user_id(user_id))

# Token d'autenticació esperat
TOKEN_VALID = "secret123"


# Token d'autenticació esperat
TOKEN_VALID = "secret123"

@app.route('/sumar', methods=['POST'])
def sumar():
    # Verificar el token
    token = request.headers.get('Authorization')
    if token != f"Bearer {TOKEN_VALID}":
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
