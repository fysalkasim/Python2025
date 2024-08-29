usernames = ["Fysal","Abin","Mubashira","Gokul","Admin"]
for username in usernames:
    if username == "Admin":
        print("Welcome back admin")
    else:
        print(f"Thank you for login {username}")

usernames2 = []
inp = input("Enter the username")
usernames2.append(inp)
if usernames2:
    for username in usernames2:
        if username == "Admin":
            print("Welcome back admin")
        else:
            print(f"Thank you for login {username}")
else:
    print("Are you sure you entered the correct username")
