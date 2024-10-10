n = int(input())
a1 = n
a2 = n
a3 = n - 2 * n % 3

if (a1 + a2 + a3) % 5 % 2 == 0:
    a1 -= (a1 + a2 + a3) % 5
elif (a1 + a2 + a3) % 5  == 3:
    a3 -= 3
elif (a1 + a2 + a3) % 5 == 1:
    a1 -= 1
    a2 -= 1
    a3 += 1

print(a1 + a2 + a3)