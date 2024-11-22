import bisect

seq = ''
ll = 0
l = 0
length = []
for i in range(1, 33000):
    seq += str(i)
    l += len(str(i))
    ll += l
    length.append(ll)

t = int(input())
for _ in range(t):
    i = int(input())
    if i == 1:
        print(1)
    else:
        indexi = bisect.bisect_left(length, i)
        print(seq[i - length[indexi - 1] - 1])