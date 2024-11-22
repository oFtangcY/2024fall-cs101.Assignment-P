d = [(2, 1), (1, 2), (1, -2), (2, -1), (-2, -1), (-1, -2), (-1, 2), (-2, 1)]

def dfs(n, m, x, y, visited):
    cnt = 0
    if len(visited) == n * m:
        return 1

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
            visited.add((nx, ny))
            cnt += dfs(n, m, nx, ny, visited)
            visited.remove((nx, ny))

    return cnt


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, m, sx, sy = map(int, input().split())

        visited = {(sx, sy)}
        print(dfs(n, m, sx, sy, visited))

