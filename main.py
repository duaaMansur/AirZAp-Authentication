import utils.session
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import mysql.connector
from db import get_db_connection
import bcrypt

# FastAPI instance
app = FastAPI()

# Pydantic model for the login request
class UserLogin(BaseModel):
    username: str
    password: str

# Function to authenticate user from the database
def authenticate_user(username: str, password: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT salt, password_hash FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    connection.close()

    if result:
        salt, stored_password_hash = result
        # Hash the input password with the stored salt
        input_password_hash = bcrypt.hashpw((password + salt).encode(), bcrypt.gensalt()).hex()
        
        if input_password_hash == stored_password_hash:
            return True
    return False

# Login route
@app.post("/login")
def login(user: UserLogin):
    if authenticate_user(user.username, user.password):
        return {"message": "Login successful!"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")
