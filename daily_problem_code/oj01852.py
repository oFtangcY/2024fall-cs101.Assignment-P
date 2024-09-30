def MinFallTime(l, location):
    move_d = location[:]
    for i in range(len(location)):
        if location[i] > l / 2:
            move_d[i] = l - location[i]
    print(max(move_d), end=' ')

def MaxFallTime(l, location):
    print(max([max(location), l - min(location)]))

def FallTime():
    l, n = map(int, input().split())
    location = list(map(int, input().split()))
    MinFallTime(l, location)
    MaxFallTime(l, location)

m = int(input())

for _ in range(m):
    FallTime()

