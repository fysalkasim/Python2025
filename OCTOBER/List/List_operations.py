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

