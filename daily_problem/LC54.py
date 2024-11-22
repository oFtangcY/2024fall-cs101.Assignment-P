class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = [[True]*(len(matrix[0]) + 2)]
        for _ in range(len(matrix)):
            visited.append([True] + [False for __ in range(len(matrix[0]))] + [True])
        visited.append([True]*(len(matrix[0]) + 2))
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        ans = []
        direction = 0
        x, y = 0, 0

        while True:
            ans.append(matrix[x][y])
            if visited[x + dx[(direction + 1) % 4] + 1][y + dy[(direction + 1) % 4] + 1] and visited[x + dx[direction] + 1][y + dy[direction] + 1]:
                break

            visited[x + 1][y + 1] = True
            nx, ny = x + dx[direction], y + dy[direction]
            if visited[nx + 1][ny + 1]:
                direction = (direction + 1) % 4

            x += dx[direction]
            y += dy[direction]


        return ans

