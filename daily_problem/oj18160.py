d = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

def dfs(x, y):
    cnt = 1
    visited[x][y] = True
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(chess) and 0 <= ny < len(chess[0]) and chess[nx][ny] == 'W' and not visited[nx][ny]:
            cnt += dfs(nx, ny)
    return cnt

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        chess = [list(input()) for _ in range(n)]
        visited = [[False for _ in range(m)] for __ in range(n)]

        maxs = 0
        for i in range(n):
            for j in range(m):
                if chess[i][j] == 'W' and not visited[i][j]:
                    maxs = max(maxs, dfs(i, j))
        print(maxs)