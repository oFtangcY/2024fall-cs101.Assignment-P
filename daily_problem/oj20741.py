from collections import deque

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def find(mapp, island, n):
    i, j = 1, 1
    while mapp[i][j] == 0 or (mapp[i][j] == 1 and (i, j) in island):
        if j == n:
            i, j = i + 1, 1
        else:
            j += 1

    return i, j


def is_valid(x, y, n):
    return 1 <= x <= n and 1 <= y <= n

def bfs(mapp, sx, sy, n):
    q = deque()
    q.append((sx, sy))
    inq = {(sx, sy)}

    while q:
        x_cur, y_cur = q.popleft()
        for dx, dy in d:
            nx, ny = x_cur + dx, y_cur + dy
            if is_valid(nx, ny, n) and mapp[nx][ny] == 1 and (nx, ny) not in inq:
                q.append((nx, ny))
                inq.add((nx, ny))

    return inq


def bridge(island_1, island_2):
    bridge_len = float('inf')
    for x_1, y_1 in island_1:
        for x_2, y_2 in island_2:
            bridge_len = min(bridge_len, abs(x_1 - x_2) + abs(y_1 - y_2) - 1)

    return bridge_len


def main():
    n = int(input())
    mapp = [[0] * (n + 2)]
    for _ in range(n):
        mapp.append([0] + list(map(int, list(input()))) + [0])
    mapp.append([0] * (n + 2))

    sx, sy = find(mapp, {}, n)
    island_1 = bfs(mapp, sx, sy, n)

    sx, sy = find(mapp, island_1, n)
    island_2 = bfs(mapp, sx, sy, n)

    print(bridge(island_1, island_2))


if __name__ == "__main__":
    main()