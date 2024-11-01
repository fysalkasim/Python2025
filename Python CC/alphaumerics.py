var = 'He@ll)2ow Worl222d'
out = 'Hellow World'
result = ''
for i in var:
    if i.isalpha() or i == ' ':
        result += i
print(result)