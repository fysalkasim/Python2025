while True:
    user = input("Enter the new password")
    alp = 0
    dig = 0
    symb = 0
    for i in user:
        if i.isalpha():
            alp+= 1
        elif i.isdigit():
            dig+= 1
        elif not i.isalnum():
            symb+= 1
    if (alp>0) and dig>0 and symb>0:
            print("Your Password Contains Alphabets, Digits and Symbols")
            break
    else:
        print("Try again")
