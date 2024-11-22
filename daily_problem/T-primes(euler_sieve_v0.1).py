import math


def euler_sieve_prime_check(n):
    if n < 2:
        return False

    is_prime = [True] * (n + 1)
    primes = []
    t_primes = set()

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            t_primes.add(i ** 2)
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            if i % p == 0:
                break

    return t_primes


n = input()
sample = list(map(int, input().split()))

t_primes = euler_sieve_prime_check(1000000)

for i in sample:
    print(['NO', 'YES'][i in t_primes])
