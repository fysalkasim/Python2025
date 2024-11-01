# numbers = [1,2,5,6,2,4,8,3,1,5,9,7]
# max(numbers)
numbers = [1, 2, 5, 6, 2, 4, 8, 3, 1, 5, 9, 7]

max_num = numbers[0] #assuming the first number as the maximum number

for number in numbers:   #iterating each elements from the list
    if number > max_num:  #checking the element is greater than the assumed maximum number
        max_num = number  #if the condition is true assign it into the max_num variable
print(max_num)     #printing the number
