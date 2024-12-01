# Assignment #9: dfs, bfs, & dp

Updated 2107 GMT+8 Nov 19, 2024

2024 fall, Complied by <mark>唐晨宇  物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 18160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/practice/18160

思路：

超级模板题……但我做了好久

把题面里的'W'看成'w'了，不管怎么搞输出都是0

一整个无语住了……浪费我半天

代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/18160.png)



### 19930: 寻宝

bfs, http://cs101.openjudge.cn/practice/19930

思路：

超级模板题$\times 2$

代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/19930.png)



### 04123: 马走日

dfs, http://cs101.openjudge.cn/practice/04123

思路：

超级模板题$\times 3$

我在尽量避免使用global，因为gpt告诉我global会使代码可维护性变差

我觉得还挺有道理的

代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/04123.png)



### sy316: 矩阵最大权值路径

dfs, https://sunnywhy.com/sfbj/8/1/316

思路：

浅设了一堆参数……至少有用

代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/sy316.png)





### LeetCode62.不同路径

dp, https://leetcode.cn/problems/unique-paths/

思路：

我发现用LeetCode类写dfs有点烦

那个\_\_init\_\_不太会用，封装类搞不太来

代码：

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [([1] + [0] * (n - 1)) for _ in range(m)]
        dp[0] = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/LC62.png)



### sy358: 受到祝福的平方

dfs, dp, https://sunnywhy.com/sfbj/8/3/539

思路：

dfs的关键还是在于”回溯“，要找到分叉路口

代码：

```python
from math import sqrt

def dfs(a):
    digits = ''
    for digit in a:
        digits += digit
        num = int(digits)
        if num > 0 and int(sqrt(num))**2 == num:
            if digits == a:
                return 1
            elif dfs(a[len(digits):]):
                return 1
            
    return 0

if __name__ == "__main__":
    A = input()

    print(['No', 'Yes'][dfs(A)])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/sy358.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

每日选做补了挺多了

Github库好久没有维护了，维护了一下

想用oi-wiki从头开始理一遍算法，找时间吧



