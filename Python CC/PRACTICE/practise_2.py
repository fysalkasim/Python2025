input = int(input("Enter the number for Buliding number"))
for i in range(1,input+1):
    for j in range(i):
        print("*", end = "")
    print()
