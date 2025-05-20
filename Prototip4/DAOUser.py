import mysql.connector

class DAOUser:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatappdam1"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def validate_user(self, identifier, password):
        query = """
            SELECT * FROM User
            WHERE (username = %s OR email = %s) AND password = %s
        """
        self.cursor.execute(query, (identifier, identifier, password))
        user = self.cursor.fetchone()
        return user

    def get_user_by_token(self, token):  # <-- ¡nuevo método!
        query = "SELECT * FROM User WHERE token = %s"
        self.cursor.execute(query, (token,))
        user = self.cursor.fetchone()
        return user

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
