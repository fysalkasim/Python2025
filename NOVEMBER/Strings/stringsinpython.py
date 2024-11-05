# # language = "python"
# # language = "java"
# # print(language)

# #Re assignment in variables

# language = "Python"
# # print(language[0])
# #   #indexing  0,1,2,3,4,5,6,7,8,9
# # print(language[0:4])

# # print(language[0:4:2])

# # slice operator = [start:stop(excluded):step]   

# # print(language[11])

# # print(len(language))

# # print(language[::-1])
# # print(language[1:5:3])

# # str = "python"
# # del str
# # print(str)

# #immutable data type

# # str1 = "Python"
# # str2  ="Language"

# # num = "1"
# # print(num*2)

# # Fruits:
# # Apple
# # Banana

# # print("""Fruits:
# # Apple
# # Banana""")

# #\t  = adding a whites space of tab

# # print("""Fruits:
# #     Apple
# #     Banana""")

# # print("Fruits\n\tAPple\n\tBanana")
# # print("Hi python\b")    #used for backspace ASCII backspace

# # print("Hi\bPython")


# # \n,\t,\b,\

# # print('He doesn\'t come')


# # print("Fruits\n\tAPple\n\tBanana")

# var1 = 10
# var2 = 1.290
# var3 = "Devansh"
# print("Integer: %sFloat:%.2f String:%s" % (var1,var2,var3))




# # f string

# var1 = 10
# var2 = 1.290
# var3 = "Devansh"

# print(f"print {var1*3},{var1*var2},{var3[0]}")
numbers = [1,2,3,4,5]

for num in numbers:
    a = numbers.pop()
    for j in numbers:
        if a%j != 0:
            print(a)
                   