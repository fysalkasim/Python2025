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


# thislist = [["apple", "kiwi", "cherry"],["Mango","banana", "cherry"]]
# # for x in thislist:
# #   for j in x:
# #     print(j)

# print(thislist[1][2])



# # thislist = ["apple", "banana", "cherry"]
# # for i in range(3):
# #   print(thislist[i])


# # print(list(range((len(str(input()))))))


# thislist = [9,81,23,1,4,7,7]
# thislist.sort()
# print(thislist)

# thislist.sort(reverse=True)
# print(thislist)

# # thislist.sort()
# # print(thislist)

# print(sorted(thislist,reverse=True))

# thislist = ["banana", "orange", "kiwi", "cherry"]
# thislist.sort()
# print(thislist)






# string1 = """738sjdfhk 
# \asvdjhasbdjkas
# asdkjhaskd
# skdkjbfsmndf
# sdjbfksf   sfsd%$Q^#%"""

# print(type(string1))






# print(language[::-1])  
#  #start index inclusive and stop index exclusive

# language[0] = "C"     #string is an immutable datatype

# language = "Cython"

# print(language)

# str2 = "python"
# del str2

# print(str2)

# language = 3
# ide = 2

# print(language*ide)


# str2 = "python"

# if "y" in str2:
#     print("y in the str2")


# str = "They said, \"Hello what's going on?\""
# print(str)

# print("Python1 \
# Python2 \
# Python3")

# print(python"Hello\nWorld")


# print("Python\nPrograming\tisfun\n")


# var1 = 10
# var2 = 1.290
# var3 = "Devansh"
# print("Integer: % Float:%f  String:%s" % (var1,var2,var3))

# count1 = "python"
# print(count1)
# print(f"{var1} is an integer here {var2} is float number ,{var3} is a string")

# str = "Hello python"
# str2 = str.count('o',7,9)
# # Displaying result
# print("occurences:", str2)

# print("data".count())


# language = "Python"

# print(language.find("n"))
# print(language.index("n"))
# str = "Java"
# str2 = "C#"
# # Calling function
# str3 = "{} and {} both are programming languages".format(str2,str)
# # Displaying result
# print(str3)


# string = "asbahdfjsd nsdfvkjhsmd"

# print(string)

# str2 =  "file.txtt"
# print(len(str2))
# print(str2.rstrip("t"))
# print(len(str2))
# print(str2)
# print(str2.rstrip())
# print(len(str2))

# str = "Java is a programming language"
# # Calling function
# str2 = str.replace("Java","C")
# print(str2)