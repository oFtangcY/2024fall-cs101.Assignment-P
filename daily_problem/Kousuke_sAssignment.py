def matchsum(a, n):
    q = set()
    q.add(0)
    suma = 0
    cnt = 0

    for i in range(n):
        suma += a[i]
        if suma in q:
            q.clear()
            cnt += 1
        q.add(suma)

    return cnt


if __name__ == "__main__":

    t = int(input())
    ans = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        ans.append(str(matchsum(a, n)))

    print('\n'.join(ans))
