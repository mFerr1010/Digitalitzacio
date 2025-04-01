import requests
import os

# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return f"Id: {self.id}, Username: {self.username}, Email: {self.email}"

# Clase UserDAO
class UserDAO:
    @staticmethod
    def login(username, password):
        response = requests.post(
            'http://127.0.0.1:5000/login',
            json={'username': username, 'password': password}
        )
        if response.status_code == 200:
            return response.json()
        else:
            print("Error:", response.json().get('error', 'Unknown error'))
            return None

# Clase ViewConsole
class ViewConsole:
    @staticmethod
    def get_input_username():
        return input("Enter username: ")

    @staticmethod
    def get_input_password():
        return input("Enter password: ")

    @staticmethod
    def show_user_info(user_data):
        print(f"\nUser Info: {user_data}")

# Función para guardar el token en un archivo
def save_token(token):
    with open("token.txt", "w") as file:
        file.write(token)

# Función para cargar el token desde un archivo
def load_token():
    if os.path.exists("token.txt"):
        with open("token.txt", "r") as file:
            return file.read().strip()
    return None

# Función para eliminar el token (cerrar sesión)
def delete_token():
    if os.path.exists("token.txt"):
        os.remove("token.txt")

# URL del endpoint
url = "http://127.0.0.1:5000/sumar"

# Verificar si ya existe un token guardado
token = load_token()
if not token:
    print("No estás autenticado. Por favor, inicia sesión.")
    username = ViewConsole.get_input_username()
    password = ViewConsole.get_input_password()
    login_response = UserDAO.login(username, password)
    if login_response:
        token = login_response['token']
        user_data = login_response['user']
        save_token(token)
        print("Inicio de sesión exitoso. Token guardado.")
        ViewConsole.show_user_info(user_data)
    else:
        print("Error al iniciar sesión.")
        exit()
else:
    print("Ya estás autenticado.")

# Preguntar si desea cerrar sesión
close_session = input("¿Deseas cerrar sesión? (s/n): ").strip().lower()
if close_session == 's':
    delete_token()
    print("Sesión cerrada. Token eliminado.")
    exit()

# Datos JSON de la petición
dades = {
    "num1": 10,
    "num2": 20
}

# Enviar petición POST
resposta = requests.post(
    url,
    json=dades,
    headers={"Authorization": token}
)

# Mostrar la respuesta del servidor
if resposta.ok:
    print("Respuesta:", resposta.json())  # {'resultat': 30}
else:
    print("Error:", resposta.status_code, resposta.text)