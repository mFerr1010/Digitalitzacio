import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="tapatappdam1"
    )

def fetch_query(query, params=None):
    connection = None
    cursor = None
    try:
        connection = connect_to_db()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def list_users_with_children():
    query = """
        SELECT 
            u.id AS user_id, 
            u.username, 
            u.email, 
            c.id AS child_id, 
            c.child_name
        FROM User u
        LEFT JOIN RelationUserChild ruc ON u.id = ruc.user_id
        LEFT JOIN Child c ON ruc.child_id = c.id
    """
    results = fetch_query(query)
    for row in results:
        print(row)

def list_taps():
    query = """
        SELECT 
            id AS tap_id,
            child_id,
            status_id,
            user_id,
            init
        FROM Tap
    """
    results = fetch_query(query)
    for row in results:
        print(row)

if __name__ == "__main__":
    print("Usuarios con hijos:")
    list_users_with_children()
    print("\nListado de Taps:")
    list_taps()
