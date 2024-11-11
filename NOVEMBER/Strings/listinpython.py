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
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist.append("jack fruit")

print(thislist)

thislist.append("jack fruit")
print(thislist)

thislist.insert(1,"jack fruit")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = "g"
thislist.extend(thistuple)
print(thislist)


list1 = [1,2,3,4,5,6]
list2 = [9,8,7,2,1]

print(list1 + list2)

# print(list2)

thislist = ["apple", "banana", "cherry","banana"]
thislist.pop()
print(thislist)