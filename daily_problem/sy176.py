n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
tot = []

i_a, i_b = 0, 0

while i_a < n or i_b < m:
    if i_a == n:
        tot.extend(B[i_b:])
        break
    if i_b == m:
        tot.extend(A[i_a:])
        break

    if A[i_a] <= B[i_b]:
        tot.append(A[i_a])
        i_a += 1
    else:
        tot.append(B[i_b])
        i_b += 1

for i in range(n + m):
    if i == n + m - 1:
        print(tot[i])
        break
    print(tot[i], end=' ')