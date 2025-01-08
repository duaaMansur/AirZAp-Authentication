import mysql.connector

# Insert a new user into the database
def insert_user(username, password):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="secureuser",
        password="securepassword",
        database="securedb"
    )
    print("Connected to the database successfully.")

    cursor = conn.cursor()
    # Directly store the username and plain-text password
    cursor.execute(
        "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
        (username, password)
    )
    conn.commit()
    print("Transaction committed successfully.")

    cursor.close()
    conn.close()

# Example usage
if __name__ == "__main__":
    username = "ddd"
    password = "ddd"
    insert_user(username, password)
