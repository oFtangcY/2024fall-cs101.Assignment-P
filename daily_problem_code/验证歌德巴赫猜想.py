x = int(input())
if x % 2 == 1 or x < 6:
    print('Error!')
else:
    prime_num = list(range(2, 2000))
    for num in range(3, 2000):
        for i in range(2, num):
            if num % i == 0:
                prime_num.remove(num)
                break
    for j in prime_num:
        if x - j in prime_num:
            print('{}='.format(x) + str(j) + '+' + str(x - j))
            prime_num.remove(x - j)