import requests

# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return f"Id: {self.id}, Username: {self.username}, Password: {self.password}, Email: {self.email}"

# Clase UserDAO
class UserDAO:
    @staticmethod
    def get_user_by_username(username):
        response = requests.get(f'http://127.0.0.1:5000/users/{username}')
        if response.status_code == 200:
            user_data = response.json()
            user = User(user_data['id'], user_data['username'], user_data['password'], user_data['email'])
            return user
        else:
            return None

# Clase ViewConsole
class ViewConsole:
    @staticmethod
    def get_input_username():
        return input("Enter username: ")

    @staticmethod
    def show_user_info(username):
        user = UserDAO.get_user_by_username(username)
        if user:
            print(f"\nUser Info: {user}")
        else:
            print(f"User with username '{username}' not found.")


if __name__ == "__main__":
    username = ViewConsole.get_input_username()
    ViewConsole.show_user_info(username)
