string = input().lower()
result = ''
for i in string:
    if i in 'aeiouy':
        continue
    else:
        result += '.' + i
print(result)