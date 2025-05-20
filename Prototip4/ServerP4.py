from flask import Flask, request, jsonify
from DAOUser import DAOUser
from DAOChild import DAOChild
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    dao_user = DAOUser()


    token = request.headers.get('Authorization')
    if token:
        user = dao_user.get_user_by_token(token)
        if user:
            return jsonify({
                "id": user['id'],
                "username": user['username'],
                "email": user['email'],
                "token": user['token'],
                "idrole": "2",
                "msg": "Usuari Ok",
                "coderesponse": "1"
            }), 200
        else:
            return jsonify({
                "coderesponse": "0",
                "msg": "No validat"
            }), 400


    data = request.get_json()
    identifier = data.get('username')
    password = data.get('password')
    user = dao_user.validate_user(identifier, password)
    if user:
        return jsonify({
            "id": user['id'],
            "username": user['username'],
            "email": user['email'],
            "token": user['token'],
            "idrole": "2",
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200
    else:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

    
@app.route('/child', methods=['POST'])
def child():
    try:
        token = request.headers.get('Authorization')
        dao_user = DAOUser()
        user = dao_user.get_user_by_token(token)

        if not user:
            return jsonify({"msg": "No validat", "coderesponse": "0"}), 400

        user_id = request.json.get('iduser')
        dao_child = DAOChild()
        children = dao_child.get_children_by_user_id(user_id)

        return jsonify({
            "msg": str(len(children)),
            "coderesponse": "1",
            "children": children
        })
    except Exception as e:
        print("Error in /child:", e) 
        return jsonify({"msg": "Server Error", "coderesponse": "0"}), 500


if __name__ == '__main__':
    app.run(debug=True)