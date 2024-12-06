def fry(t, k):
    maxt = sum(t) / k
    if t[0] > maxt:
        maxt = fry(t[1:], k - 1)

    return maxt

if __name__ == "__main__":
    n, k = map(int, input().split())
    t = sorted(list(map(int, input().split())), reverse=True)

    maxt = fry(t, k)
    print('{:.3f}'.format(maxt))