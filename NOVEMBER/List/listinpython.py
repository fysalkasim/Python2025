# # mutable
# # add, remove,join,modification allowed

# # ordered  , indexed, duplictes allo

# thislist = [1,2,3,4,5,6]
# print(thislist)

# print(type(list))

# thislist = [1,2,3,4,5,6]
# thislist = [1.0,2.0]
# thislist = ["AABc","AHSG"]
# thislist = [True,False]

# thislist2 = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist2)
# print(str("123"))

# print(list("python"))



# thislist = [9,5,6,2,7,2,3,1,1,2,4125,9]

# print(sorted(thislist))
# print(thislist)

# print(thislist[::2])


# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# print(len(thislist))
# thislist[1:3] = ["blackcurrant"]
# print(thislist)
# print(len(thislist))
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

# thislist.append("jack fruit")

# print(thislist)

# thislist.append("jack fruit")
# print(thislist)

# thislist.insert(1,"jack fruit")
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thistuple = "g"
# thislist.extend(thistuple)
# print(thislist)


# list1 = [1,2,3,4,5,6]
# list2 = [9,8,7,2,1]

# print(list1 + list2)

# # print(list2)

# thislist = ["apple", "banana", "cherry","banana"]
# thislist.pop()
# print(thislist)


# thislist = ["apple", "banana", "cherry"]

# # thislist.remove("cherry")

# print(thislist)

# newlist = thislist.copy()

# print(newlist)

# newlist.pop(0)

# print(newlist)
# print(thislist)


# numeric_str = "½"
# print(numeric_str.isnumeric())


# thislist = [1,2,6,8,4,2,3]

# square = []

# for i in thislist:
#     j = i*i
#     square.append(j)

# print(square)
# np = [1,3,5,6,87,9]

# squares = [i**2 for i in np ]
# print(squares)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)


# newlist = [x for x in range(1,10000) if x %2 ==0 and x %4 == 0 and x%576 == 0]

# print(newlist)
