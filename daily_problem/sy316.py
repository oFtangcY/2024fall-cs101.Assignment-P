d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def dfs(n, m, x, y, mat, visited, path_sum, path):
    global max_path, maxs
    if x == n - 1 and y == m - 1:
        if path_sum > maxs:
            maxs = path_sum
            max_path = path
            
        return
    
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(n, m, nx, ny, mat, visited, path_sum + mat[nx][ny], path + [(nx, ny)])
            visited[nx][ny] = False

    return 


if __name__ == "__main__":
    n, m = map(int, input().split())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))

    visited = [[False for _ in range(m)] for __ in range(n)]
    visited[0][0] = True
    max_path = []
    INF = float('inf')
    maxs = -INF
    dfs(n, m, 0, 0, mat, visited, mat[0][0], [(0, 0)])
    for x, y in max_path:
        print(x + 1, y + 1)