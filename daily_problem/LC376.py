class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for i in range(n)] for j in range(m)]
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]
        direction = 0
        x, y = 0, 0
        ans = []

        while True:
            ans.append(matrix[x][y])
            visited[x][y] = True
            if visited[x + dx[(direction + 1) % 4]][y + dy[(direction + 1) % 4]]:
                return ans

            if not (x + dx[direction] < m and y + dy[direction] < n and not visited[max(x + dx[direction], m - 1)][
                max(y + dy[direction], n - 1)]):
                direction = (direction + 1) % 4

            x += dx[direction]
            y += dy[direction]


