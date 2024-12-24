# Assignment #D: 十全十美 

Updated 1254 GMT+8 Dec 17, 2024

2024 fall, Complied by <mark>唐晨宇  物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 02692: 假币问题

brute force, http://cs101.openjudge.cn/practice/02692

思路：

之前看到过一次，但是没做

这次思路比较清晰，这种题目主要拼细节

一遍过

代码：

```python
coins = {'L', 'F', 'E', 'J', 'I', 'D', 'K', 'C', 'G', 'H', 'A', 'B'}

def meansure_heavy(items, res, coins):
    for coin in coins:
        for i in range(3):
            if (coin in items[i][0] and res[i] == 'up') or (coin in items[i][1] and res[i] == 'down') or (
                    coin not in items[i][0] and coin not in items[i][1] and res[i] == 'even'):
                ans = True
            else:
                ans = False
                break

        if ans:
            return f'{coin} is the counterfeit coin and it is heavy.'

    return None

def meansure_light(items, res, coins):
    for coin in coins:
        for i in range(3):
            if (coin in items[i][0] and res[i] == 'down') or (coin in items[i][1] and res[i] == 'up') or (
                    coin not in items[i][0] and coin not in items[i][1] and res[i] == 'even'):
                ans = True
            else:
                ans = False
                break

        if ans:
            return f'{coin} is the counterfeit coin and it is light.'

    return None

def main():
    n = int(input())
    for _ in range(n):
        items, res = [], []
        for __ in range(3):
            l, r, result = input().split()
            items.append([l, r])
            res.append(result)

        ans1 = meansure_heavy(items, res, coins)
        ans2 = meansure_light(items, res, coins)
        if ans1:
            print(ans1)
        else:
            print(ans2)

if __name__ == '__main__':
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](02692.png)



### 01088: 滑雪

dp, dfs similar, http://cs101.openjudge.cn/practice/01088

思路：

又是对着答案做阅读理解的一天

不过这个思路还挺好理解的，就是没想到

逆向的一个思维，关键还是在于dp的核心就是母结构操作不影响子结构最优选择

代码：

```python
import heapq

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def main():
    r, c = map(int, input().split())
    mapp = [list(map(int, input().split())) for _ in range(r)]

    heap = []
    for i in range(r):
        for j in range(c):
            heap.append((mapp[i][j], i, j))
    heapq.heapify(heap)

    dp = [[1] * c for _ in range(r)]
    longest_path = 1

    while heap:
        h, x, y = heapq.heappop(heap)
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and mapp[nx][ny] < h:
                dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)

        longest_path = max(longest_path, dp[x][y])

    print(longest_path)

if __name__ == '__main__':
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](01088.png)



### 25572: 螃蟹采蘑菇

bfs, dfs, http://cs101.openjudge.cn/practice/25572/

思路：

思路还是比较清晰的，似乎并不难，就是题面比较新颖

一遍过

代码：

```python
from collections import deque


d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def bfs(mapp, sx, sy, di, dj):
    q = deque()
    q.append((sx, sy))
    inq = set()
    inq.add((sx, sy))

    while q:
        x_cur, y_cur = q.popleft()

        if mapp[x_cur][y_cur] == 9 or mapp[x_cur + di][y_cur + dj] == 9:
            return 'yes'

        for dx, dy in d:
            nx, ny = x_cur + dx, y_cur + dy
            if (nx, ny) not in inq and mapp[nx][ny] != 1 and mapp[nx + di][ny + dj] != 1:
                q.append((nx, ny))
                inq.add((nx, ny))

    return 'no'

def main():
    n = int(input())
    mapp = [[1] * (n + 2)] + [([1] + list(map(int, input().split())) + [1]) for _ in range(n)] + [[1] * (n + 2)]
    for i in range(n + 2):
        for j in range(n + 2):
            if mapp[i][j] == 5:
                sx, sy = i, j
                for dx, dy in d:
                    if mapp[i + dx][j + dy] == 5:
                        di, dj = dx, dy
                        break
                break

    print(bfs(mapp, sx, sy, di, dj))

if __name__ == '__main__':
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](25572.png)



### 27373: 最大整数

dp, http://cs101.openjudge.cn/practice/27373/

思路：

这么多排序算法……我只会sort

qaq

冒泡排序有点复杂，看上去很好理解其实数学证明应该还挺复杂的？

代码：

```python
from functools import cmp_to_key


def sorting(x: str, y: str):
    if int(x + y) > int(y + x):
        return -1
    else:
        return 1

def main():
    m = int(input())
    n = int(input())
    num = input().split()
    num.sort(key=cmp_to_key(sorting))

    dp = [''] + ['!'] * m
    for i in range(n):
        for j in range(m, len(num[i]) - 1, -1):
            if dp[j - len(num[i])] != '!':
                if dp[j] == '!' or int(dp[j - len(num[i])] + num[i]) > int(dp[j]):
                    dp[j] = dp[j - len(num[i])] + num[i]

    for i in range(m, 0, -1):
        if dp[i] != '!':
            print(dp[i])
            break

if __name__ == '__main__':
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](27373.png)



### 02811: 熄灯问题

brute force, http://cs101.openjudge.cn/practice/02811

思路：

确实是没有想到这个枚举思路

考虑数学上的叠加解法也没有想到解线性方程>_<吐了

能用numpy的话解个矩阵方程不是手拿把掐

代码：

```python
from copy import deepcopy
from itertools import product

change = {0: 1, 1: 0}
p_mat = [[0] * 8] + [[0, *map(int, input().split()), 0] for i in range(5)] + [[0] * 8]

for change_row_1 in product(range(2), repeat=6):
    mat = deepcopy(p_mat)
    operate = [list(change_row_1)]
    for i in range(1, 6):
        for j in range(1, 7):
            if operate[i - 1][j - 1]:
                mat[i][j] = change[mat[i][j]]
                mat[i - 1][j] = change[mat[i - 1][j]]
                mat[i + 1][j] = change[mat[i + 1][j]]
                mat[i][j - 1] = change[mat[i][j - 1]]
                mat[i][j + 1] = change[mat[i][j + 1]]
        operate.append(mat[i][1:7])
    if mat[5][1:7] == [0] * 6:
        for op_ in operate[:-1]:
            print(' '.join(map(str, op_)))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](02811.png)



### 08210: 河中跳房子

binary search, greedy, http://cs101.openjudge.cn/practice/08210/

思路：

刚开始还一直在尝试用递归实现……TLE

改成优先队列还是TLE

就只能迭代是吧……我也想不出这个算法啊

代码：

```python
#AC
def check(x, n, m,  stones):
    num, stone_cur = 0, 0
    for i in range(1, n + 2):
        if stones[i] - stone_cur < x:
            num += 1
        else:
            stone_cur = stones[i]

    if num > m:
        return True
    else:
        return False

def main():
    l, n, m = map(int, input().split())
    stones = [0] + [int(input()) for _ in range(n)] + [l]

    lo, hi = 0, l + 1
    ans = -1
    while lo < hi:
        mid = (lo + hi) // 2

        if check(mid, n, m, stones):
            hi = mid
        else:
            ans = mid
            lo = mid + 1

    print(ans)



if __name__ == '__main__':
    main()
    
#TLE
from heapq import heapify


def pop_stone(d_stone):
    d_stone_copy = d_stone[:]
    heapify(d_stone_copy)
    d, i = d_stone_copy[0]

    if i == 0:
        d_stone_new = [(d + d_stone[1][0], 0)]
        for j in range(2, len(d_stone)):
            d_stone_new.append((d_stone[j][0], j - 1))
    elif i == len(d_stone):
        d_stone_new = d_stone[:-2]
        d_stone_new[-1][0] += d
    else:
        if min(d + d_stone[i + 1][0], d_stone[i - 1][0]) >= min(d + d_stone[i - 1][0], d_stone[i + 1][0]):
            d_stone_new = []
            for j in range(len(d_stone)):
                if j < i:
                    d_stone_new.append((d_stone[j][0], j))
                elif j == i + 1:
                    d_stone_new.append((d_stone[j][0] + d, j - 1))
                elif j > i + 1:
                    d_stone_new.append((d_stone[j][0], j - 1))
        else:
            d_stone_new = []
            for j in range(len(d_stone)):
                if j < i - 1:
                    d_stone_new.append((d_stone[j][0], j))
                elif j == i - 1:
                    d_stone_new.append((d_stone[j][0] + d, j))
                elif j > i:
                    d_stone_new.append((d_stone[j][0], j - 1))

    return d_stone_new

def main():
    l, n, m = map(int, input().split())
    l_stone, d_stone = [], []
    l_stone.append(0)
    for i in range(1, n + 1):
        l_stone.append(int(input()))
        d_stone.append((l_stone[i] - l_stone[i - 1], i - 1))
    d_stone.append((l - l_stone[-1], n))

    for _ in range(m):
        d_stone = pop_stone(d_stone)

    heapify(d_stone)
    print(d_stone[0][0])

if __name__ == '__main__':
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](08210.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

我现在觉得上面这句如果<mark>如果作业题目简单</mark>简直就是在嘲讽我

它对我造成了极大的心理伤害！拒绝PUA！

这个作业是一点做不来……就弄出来两道，感觉机考完蛋的节奏

不过这两道都是一遍AC的，这还是近一个月来第一次……虽然这一个月左右时间题目做的也挺少的吧



