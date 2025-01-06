import hashlib

# A simple in-memory storage for users
database = {}

def hash_password(password):
    """Hashes a password for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    """Registers a new user with a username and password."""
    if username in database:
        return "Error: Username already exists."
    hashed_password = hash_password(password)
    database[username] = hashed_password
    return "Registration successful."

def login(username, password):
    """Logs in a user by checking their username and password."""
    if username not in database:
        return "Error: Username does not exist."
    hashed_password = hash_password(password)
    if database[username] != hashed_password:
        return "Error: Incorrect password."
    return "Login successful."

def secured_page(username):
    """Accesses a secured page only if the user is logged in."""
    if username in database:
        return f"Welcome to the secured page, {username}!"
    return "Error: You must log in first."

# Example usage
if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Register")
        print("2. Login")
        print("3. Access Secured Page")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            user = input("Enter username: ")
            pwd = input("Enter password: ")
            print(register(user, pwd))
        elif choice == "2":
            user = input("Enter username: ")
            pwd = input("Enter password: ")
            print(login(user, pwd))
        elif choice == "3":
            user = input("Enter username: ")
            print(secured_page(user))
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
