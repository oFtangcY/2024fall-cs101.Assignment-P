ans = []

def arrange(seq, arr):
    q = set()
    if len(arr) == n:
        ans.append(arr)
        return

    for i in range(n):
        if visited[i] == 1 or seq[i] in q:
            continue
        else:
            q.add(seq[i])
            visited[i] = True
            arrange(seq, arr + [seq[i]])
            visited[i] = False


if __name__ == '__main__':
    n = int(input())
    a = sorted(list(map(int, input().split())))
    visited = [False] * n

    arrange(a, [])
    for arr in ans:
        print(' '.join(map(str, arr)))
