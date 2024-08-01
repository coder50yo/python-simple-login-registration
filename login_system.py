import hashlib
import os

class UserSystem:
    def __init__(self):
        self.users = {}

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register_user(self, username, password):
        if username in self.users:
            raise ValueError("User already exists")
        hashed_password = self.hash_password(password)
        self.users[username] = hashed_password
        return "User registered successfully"

    def login_user(self, username, password):
        hashed_password = self.hash_password(password)
        if username not in self.users:
            raise ValueError("User does not exist")
        if self.users[username] != hashed_password:
            raise ValueError("Incorrect password")
        return "User logged in successfully"

if __name__ == "__main__":
    user_system = UserSystem()
    while True:
        action = input("Do you want to register or login? (register/login): ").strip().lower()
        if action not in ["register", "login"]:
            print("Invalid action. Please choose 'register' or 'login'.")
            continue
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        try:
            if action == "register":
                print(user_system.register_user(username, password))
            elif action == "login":
                print(user_system.login_user(username, password))
        except ValueError as e:
            print(e)
