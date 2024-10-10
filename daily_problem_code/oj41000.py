k = int(input())

for _ in range(k):
    n = int(input())
    time = [set(map(int, input().split()))]
    for __ in range(n - 1):
        s, d = map(int, input().split())
        for i in range(len(time)):
            if set(range(s, d + 1)).intersection(time[i]) != set():
                time[i] = set(range(s, d + 1)).intersection(time[i])
                break
        else:
            time.append(set(range(s, d + 1)))
    print(len(time))
