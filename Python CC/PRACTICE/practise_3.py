numbers = []
while True:
    num = (int(input("Enter the number to add in the list or 0 to quit  ")))
    if num != 0:
        numbers.append(num)
    else:
        break
print("These are the numbers you entered", numbers)

even = []
odd = []
for i in numbers:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("These are the even numbers",even)
print("These are the odd numbers",odd)

