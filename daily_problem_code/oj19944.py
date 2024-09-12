import math

def translate(c, y, m, d):
    w = (y + math.floor(y / 4) + math.floor(c / 4) - 2 * c + math.floor(2.6 * (m + 1)) + d - 1) % 7
    return w

n = int(input())
result = []
dig_weekday = {0 : 'Sunday', 1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Saturday'}
for _ in range(n):
    date = input()
    c = int(date[0:2])
    d = int(date[-2:])
    if date[4:6] == '01' or date[4:6] == '02':
        if date[2:4] == '00':
            y = 99
            c -= 1
        else:
            y = int(date[2:4]) - 1
        m = int(date[4:6]) + 12
    else:
        y = int(date[2:4])
        m = int(date[4:6])
    result.append(dig_weekday.get(translate(c, y, m, d)))
for ans in result:
    print(ans)
