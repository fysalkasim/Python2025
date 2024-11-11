# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Vicky")
# print(dict(zip(a,b)))  [[]]

# help(zip())


# def functionname():
#     """Creating a function that welcomes to python"""
#     return "Welcome to python"

# pp = functionname()
# print(pp)

# inp = input("enter the name")
# name = "python"
# print(name)

#required arguments

# print(len())

# def add(num1,num2):
#     return num1+num2

# print(add(1,2))
# print(add(1,2,3))

# def add():
#     return 5+4

# print(add())
# print(add(1))

# def favc(name,colour):
#     return name+colour

# print(favc("fysal","blue"))

# print(favc(1,2))

# print(favc({1,2,3},{1,4,5}))




# favc("fysal","blue")

# favc("blue","fysal")
def favc(name,colour,year):
    print(f"{name}'s favorite colour is {colour}")
    print(year)

# favc(colour="blue",name="fysal",2024)
# favc("fysal","blue",year=2024)

# def power(number,power=2):
#     print(number**power)


# power(power=3,number=2)

# def printme(*names):
#     for name in names:
#         print(name)
# printme()

# def group(members,*names):
#     print("There will be",members,"of members")
#     for i in names:
#         print(i)

# group(5,"fysal","sree","reethu","shalu")


def student(name,**info):
    # print(name)
    info.update({"name":name})
    print(info)

student("fysal",Blood="o+",home="kaloor")

