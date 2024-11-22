import math


def euler_sieve_prime_check(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            if i % p == 0:
                break

    return is_prime


def CheckTPrime(x):
    sqrt_x = int(math.sqrt(x))
    if sqrt_x ** 2 == x:
        if is_prime[sqrt_x]:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'


n = input()
sample = list(map(int, input().split()))

is_prime = euler_sieve_prime_check(1000000)

for i in sample:
    print(CheckTPrime(i))
