mylist = [1,2,3,2,1,3,4,2]
mylist2 = []
j = 0
for i in mylist:
    if i not in mylist2:
        mylist2+=[i]
        j+=1
print(mylist2)

# mylist = [1, 2, 3, 2, 1, 3, 4, 2]
# mylist2 = []
# j = 0
# for i in mylist:
#     if i not in mylist2:
#         # mylist2 += [None]  # Increase the size of mylist2 by one
#         mylist2[j] = i     # Assign value to the new index
#         j += 1
# print(mylist2)

# list2 = [1,2,3,4]
# list2[4] = 5
# print(list2)
# mylist = [1, 2, 3, 2, 1, 3, 4, 2]
# mylist2 = []
# j = 0
# for i in mylist:
#     if i not in mylist2:
#         mylist2 += [None]  # Increase the size of mylist2 by one
#         mylist2[j] = i
#         j+= 1
# print(mylist2)

# mylist = [1, 2, 3, 2, 1, 3, 4, 2]
# mylist2 = []
# j = 0
# for i in mylist:
#     if i not in mylist2:
#         print(i)  # Properly indented
# mylist = [1, 2, 3, 2, 1, 3, 4, 2]
# mylist2 = []
# for i in mylist:
#     if i not in mylist2:
#         print(i)  # Print the unique element
#         mylist2.append(i)  # Add the unique element to mylist2
