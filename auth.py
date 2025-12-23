import json
import hashlib
import os

USERS_FILE = "users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def signup(username, password):
    users = load_users()
    if username in users:
        return False, "User already exists"
    
    users[username] = hash_password(password)
    save_users(users)
    return True, "Signup successful"

def login(username, password):
    users = load_users()
    if username not in users:
        return False, "User not found"
    
    if users[username] == hash_password(password):
        return True, "Login successful"
    
    return False, "Wrong password"
