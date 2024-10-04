i = 0
while True:
    password =input("enter the passoword")
    if password != "password":
        i += 1
        print("try again")
    if i == 3:
        print("You have been blocked")
        break
    if password == "password":
        print("you are logged in")
        break