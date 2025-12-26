def register():
    user = input("Username: ")
    pwd = input("Password: ")
    with open("user.txt", "a") as f:
        f.write(user + "," + pwd + "\n")
    print("Registered successfully")

def login():
    user = input("Username: ")
    pwd = input("Password: ")
    with open("user.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == user and p == pwd:
                print("Login success")
                return
    print("Login failed")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    c = input("Choose: ")

    if c == "1":
        register()
    elif c == "2":
        login()
    elif c == "3":
        break
