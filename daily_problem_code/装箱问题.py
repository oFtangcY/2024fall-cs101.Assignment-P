def CheckRemain(x):
    if x < 0:
        return 0
    else:
        return x

def SpaceOf3_3Remain(c):
    remain2 = [0, 5, 3, 1][c % 4]
    remain1 = [0, 7, 6, 5][c % 4]
    return [remain1, remain2]

def LeastBox(c, d, e, f):
    return f + d + e + (c + 3) // 4

def Remain1And2Box(a, b):
    box = b // 9 + a // 36
    remain = b % 9 * 4 + a % 36
    if remain > 36:
        box += 2
    elif remain == 0:
        box += 0
    else:
        box += 1
    return box

while True:
    a, b, c, d, e, f = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
        break
    else:
        b -= 5 * d + SpaceOf3_3Remain(c)[1]
        a -= 11 * e + SpaceOf3_3Remain(c)[0]
        if b < 0:
            a += 4 * b

        b = CheckRemain(b)
        a = CheckRemain(a)
        print(LeastBox(c, d, e, f) + Remain1And2Box(a, b))