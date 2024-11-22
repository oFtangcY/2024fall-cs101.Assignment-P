from collections import deque

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
def bfs(x, y, mapp):
    q = deque()
    q.append((0, (x, y)))
    inq = {(x, y)}

    while q:
        step, (cur_x, cur_y) = q.popleft()
        if mapp[cur_x][cur_y] == 1:
            return step
        
        for dx, dy in d:
            nx, ny = cur_x + dx, cur_y + dy
            if mapp[nx][ny] != 2 and (nx, ny) not in inq:
                q.append((step + 1, (nx, ny)))
                inq.add((nx, ny))

    return 'NO'


if __name__ == '__main__':
    m, n = map(int, input().split())
    mapp = [[2]*(n + 2)]
    for _ in range(m):
        mapp.append([2] + list(map(int, input().split())) + [2])
    mapp.append([2]*(n + 2))

    print(bfs(1, 1, mapp))