t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(min(n * min(b) + sum(a), n * min(a) + sum(b)))