lucky_num = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
n = int(input())

ans = 'NO'
for i in lucky_num:
    if n % i == 0:
        ans = 'YES'

print(ans)