str1 = list(input().lower())
str2 = list(input().lower())
n = len(str1)
if str1 == str2:
    print('0')
for i in range(0, n):
    if ord(str1[i]) < ord(str2[i]):
        print('-1')
        break
    if ord(str1[i]) > ord(str2[i]):
        print('1')
        break