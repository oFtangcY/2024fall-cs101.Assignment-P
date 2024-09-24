def EvenOperate(a):
    b = a // 2
    print('{}/2={}'.format(a, b))
    return b

def OddOperate(a):
    b = a * 3 + 1
    print('{}*3+1={}'.format(a, b))
    return b

x = int(input())
while x != 1:
    if x % 2 == 0:
        x = EvenOperate(x)
    else:
        x = OddOperate(x)
