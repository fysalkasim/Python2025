names = ["Reethu","Sreelekshmi","Sreekutty","Salu"]

age = [10,12,14,16]

print(type(names))
print(type(age))

print(names)
print(age)

print(names[-1])

names = ["Reethu","Sreelekshmi","Sreekutty","Salu","Lekshmi"]

print(len(names))


course = "Data_Analytics"

print(list(course))

course = list(course)
print(course)

del names[-1]
print(names)



names = ["Reethu","Sreelekshmi","Sreekutty","Salu"]
print(sorted(names))
numbers = [1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6]

print(numbers)
print(len(numbers))

numbers[2:7] = [10,11,21]
print(numbers)
print(len(numbers))

numbers.append(5)
print(numbers)
# assignment 16
player_names = ["Rohit","Sachin","Dhoni","Virat","Rahul"]
jersey_number = [9,10,7,5,8]
print("Type of first list(player_names) :",type(player_names))
print("Type of second list(jersey_number) :",type(jersey_number))

print("First three players :",player_names[:3])
print("Last two players :",player_names[:-3:-1])
print("Every second players :",player_names[::2])

#delete one player
del player_names[1]
del jersey_number[1]
print("After removing player 'Sachin' from the list :",list(player_names),list(jersey_number))

#add a new player
player_names = ["Rohit","Dhoni","Virat","Rahul","Bumrah"]
jersey_number = [9,7,5,8,11]
print("List after adding a new player :",player_names,jersey_number)

#add a duplicate value
player_names = ["Rohit","Dhoni","Virat","Rahul","Bumrah","Dhoni"]
jersey_number = [9,7,5,8,11,1]
print("Length of the list :",len(player_names))

#player name sorted alphabetically
print("Sorted list : ",sorted(player_names))
#jersey number sorted in ascending order
print("Sorted list :",sorted(jersey_number))