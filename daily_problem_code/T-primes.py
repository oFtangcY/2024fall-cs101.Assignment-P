import math

def era_sieve():

    is_prime = [1] * (10**6)
    t_prime = set()

    for i in range(2, 10**6):
        if is_prime[i]:
            t_prime.add(i ** 2)
            for j in range(i * i, 10**6, i):
                is_prime[j] = 0

    return t_prime

t_prime = era_sieve()

input()
for i in map(int, input().split()):
    print(['NO', 'YES'][i in t_prime])


