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
# numbers = [1,2,3,4,5]

# for num in numbers:
#     a = numbers.pop()
#     for j in numbers:
#         if a%j != 0:
#             print(a)
# language = "ppppyt sd12121"
# # print(language.count('p',4))
# # print(language.find("z"))
# print(language.isalnum())
# print(language.isalpha())

# spaces = " sdad  "
# print(spaces.isspace())
# print(language.title())

# str =  "  python  "
# # Calling function
# str2 = str.lstrip()
# print(str2)

# str = "Java is a programming language"
# # Calling function
# str2 = str.split("a")
# # Displaying result
# print(str)
# print(str2)


# 1-50 3,5 divide numbers
# for i in range(1,50):
#     if i%3 == 0 and i%5==0 :
#         print(i)

# i = 0
# while i < 30:
#     if i == 10:
#         i += 1
#         continue
#     print('Current number :', i)
#     i += 1
# n = 10

# if n > 10:
#     pass

# print('Hello')


# py = "python"
# lv = list(py)

# del lv[0]
# print(lv)

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   for j in x:
#     print(j)


thislist = [["apple", "kiwi", "cherry"],["Mango","banana", "cherry"]]
# for x in thislist:
#   for j in x:
#     print(j)

print(thislist[1][2])



# thislist = ["apple", "banana", "cherry"]
# for i in range(3):
#   print(thislist[i])


# print(list(range((len(str(input()))))))


thislist = [9,81,23,1,4,7,7]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

# thislist.sort()
# print(thislist)

print(sorted(thislist,reverse=True))

thislist = ["banana", "orange", "kiwi", "cherry"]
thislist.sort()
print(thislist)
