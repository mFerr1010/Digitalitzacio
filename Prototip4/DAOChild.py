import mysql.connector

class DAOChild:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="tapatappdam1"
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_children_by_user_id(self, user_id):
        query = """
            SELECT c.id, c.child_name, c.sleep_average, c.treatment_id, c.time
            FROM Child c
            INNER JOIN RelationUserChild r ON c.id = r.child_id
            WHERE r.user_id = %s
        """
        self.cursor.execute(query, (user_id,))
        children = self.cursor.fetchall()
        return children

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
