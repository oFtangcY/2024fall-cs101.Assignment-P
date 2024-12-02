# Assignment #A: dp & bfs

Updated 2 GMT+8 Nov 25, 2024

2024 fall, Complied by <mark>唐晨宇 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：

嗯~常规dp

代码：

```python
N = int(input())
dp = [-1] * (N + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](P1255.png)



### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：

常规dp$\times$2

代码：

```python
N = int(input())
dp = [1] * (N + 1)

for i in range(2, N + 1):
    for j in range(1, i):
        dp[i] += dp[i - j]

print(dp[N])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](oj27528.png)



### 474D. Flowers

dp, https://codeforces.com/problemset/problem/474/D

思路：

其实思路同上两题……题面描述的比较复杂，但并没啥问题

代码：

```python
MOD = 1000000007

def dinner(k):
    dp = [1] * 100007
    for i in range(k, 100001):
        dp[i] = (dp[i - k] + dp[i - 1]) % MOD

    prefix = [0] * 100007
    prefix[0] = dp[0]
    for i in range(1, 100007):
        prefix[i] = (prefix[i - 1] + dp[i]) % MOD

    return dp, prefix

if __name__ == "__main__":
    t, k = map(int, input().split())
    dp, prefix = dinner(k)
    
    for _ in range(t):
        a, b = map(int, input().split())
        if a == 0:
            print(prefix[b] % MOD)
        else:
            print((prefix[b] - prefix[a - 1]) % MOD)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](LC5.png)



### LeetCode5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：

朴素的“遍历”，但似乎可以优化（我还没仔细看答案）

代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        longest_str = s[0]
        maxlen = 1
        for i in range(n):
            dp[i][i] = True
            if i != n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                maxlen = 2
                longest_str = s[i] + s[i + 1]
    
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and maxlen < j - i + 1:
                    maxlen = j - i + 1
                    longest_str = s[i:j + 1]

        return longest_str
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](LC5-1733155893141-6.png)





### 12029: 水淹七军

bfs, dfs, http://cs101.openjudge.cn/practice/12029/

思路：

我承认我抄答案了……等我好好debug一下.

弄了好久~你的广搜我的广搜好像不一样

代码：

```python
from collections import deque
import sys

def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n


def bfs(start_x, start_y, start_height, m, n, h, water_height):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque([(start_x, start_y, start_height)])
    water_height[start_x][start_y] = start_height

    while q:
        x, y, height = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if is_valid(nx, ny, m, n) and h[nx][ny] < height:
                if water_height[nx][ny] < height:
                    water_height[nx][ny] = height
                    q.append((nx, ny, height))


def main():
    data = sys.stdin.read().split()
    idx = 0
    k = int(data[idx])
    idx += 1
    results = []

    for _ in range(k):
        m, n = map(int, data[idx:idx + 2])
        idx += 2
        h = []
        for i in range(m):
            h.append(list(map(int, data[idx:idx + n])))
            idx += n
        water_height = [[0] * n for _ in range(m)]

        i, j = map(int, data[idx:idx + 2])
        idx += 2
        i, j = i - 1, j - 1

        p = int(data[idx])
        idx += 1

        for _ in range(p):
            x, y = map(int, data[idx:idx + 2])
            idx += 2
            x, y = x - 1, y - 1
            if h[x][y] <= h[i][j]:
                continue
            bfs(x, y, h[x][y], m, n, h, water_height)

        results.append("Yes" if water_height[i][j] > 0 else "No")

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](oj12029.png)



### 02802: 小游戏

bfs, http://cs101.openjudge.cn/practice/02802/

思路：

inq集合记录的是经历过的“状态”！！

纯唐……我RE的主要原因是表达式里的pair打成了part

代码：

```python
from collections import deque

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
INF = float('inf')

def is_valid(x, y, w, h):
    return 0 <= x < h + 2 and 0 <= y < w + 2


def bfs(sx, sy, ex, ey, cards, w, h):
    seg = INF
    q = deque()
    q.append((sx, sy, 0, 0, 0))
    inq = {((sx, sy), (0, 0))}

    while q:
        x_cur, y_cur, x_move, y_move, step = q.popleft()

        for dx, dy in d:
            nx, ny = x_cur + dx, y_cur + dy
            if nx == ex and ny == ey:
                if dx == x_move and dy == y_move:
                    seg = min(seg, step)
                else:
                    seg = min(seg, step + 1)
                continue

            if is_valid(nx, ny, w, h) and cards[nx][ny] == ' ' and ((nx, ny), (dx, dy)) not in inq:
                inq.add(((nx, ny), (dx, dy)))
                if dx == x_move and dy == y_move:
                    q.append((nx, ny, dx, dy, step))
                else:
                    q.append((nx, ny, dx, dy, step + 1))

    if seg == INF:
        return 'impossible'
    else:
        return f'{seg} segments'
    
def main():
    board = 0
    while True:
        board += 1
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        cards = [[' ']*(w + 2)]
        for _ in range(h):
            cards.append([' '] + list(input()) + [' '])
        cards.append([' ']*(w + 2))

        print(f'Board #{board}:')
        pair = 0
        while True:
            pair += 1
            x1, y1, x2, y2 = map(int, input().split())
            if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
                break

            print(f'Pair {pair}: ' + bfs(y1, x1, y2, x2, cards, w, h) + '.')
        print()


if __name__ == "__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](oj02802.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

后面复杂的dfs和bfs问题基本形式都不太难，但就是过不了

你会发现有非常多的细节需要考虑到，一个地方出错就会有很多问题

还是题做少了>_<但是真的很忙



