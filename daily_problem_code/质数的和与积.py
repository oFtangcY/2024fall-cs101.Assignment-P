import math

def era_sieve():

    is_prime = [1] * (10**5)

    for i in range(2, 10**5):
        if is_prime[i]:
            for j in range(i * 2, 10**5, i):
                is_prime[j] = 0

    return is_prime

is_prime = era_sieve()

s = int(input())

for i in range(s // 2, 1, -1):
    if is_prime[i] and is_prime[s - i]:
        print(i * (s - i))
        break