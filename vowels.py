cnt = 0
vowels = ['a','e','i','o','u']
var = 'Hello World'
for i in var.lower():
    if i in vowels:
        cnt += 1
print(cnt)
