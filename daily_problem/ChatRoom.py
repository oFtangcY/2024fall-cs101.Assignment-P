s = list(input())
key = 'hello'
j = 0
while True:
    try:
        i = s.index(key[j])
        j += 1
        del s[:i + 1]
        if j == 5:
            print('YES')
            break
    except ValueError:
        print('NO')
        break