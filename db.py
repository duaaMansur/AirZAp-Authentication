import mysql.connector

# Database connection function
def get_db_connection():
    connection = mysql.connector.connect(
        host="db",  # Docker service name or localhost
        user="secureuser",
        password="securepassword",
        database="securedb"
    )
    return connection
