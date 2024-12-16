# Assignment #C: 五味杂陈 

Updated 1148 GMT+8 Dec 10, 2024

2024 fall, Complied by <mark>唐晨宇 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 1115. 取石子游戏

dfs, https://www.acwing.com/problem/content/description/1117/

思路：

用了一下题目给的提示，直接给他干成贪心了……

代码：

```python
import sys

if __name__ == '__main__':
    ind = 0
    data = list(map(int, sys.stdin.read().split()))
    while data[ind] != 0 and data[ind + 1] != 0:
        a, b = max(data[ind], data[ind + 1]), min(data[ind], data[ind + 1])
        if a // b == 1:
            if a == b:
                print('win')
            else:
                round = 0
                while a // b < 2:
                    round += 1
                    a, b = min(a, b), max(a, b) % min(a, b)
                print(['win', 'lose'][round % 2])
        else:
            print('win')
        ind += 2
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](acw1115.png)



### 25570: 洋葱

Matrices, http://cs101.openjudge.cn/practice/25570

思路：

仅仅涉及到矩阵的题目都不难的样子，但是有时候要考虑周全

代码：

```python
import math

if __name__ == '__main__':
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))

    if n % 2 == 0:
        mx, my = (n - 1) / 2, (n - 1) / 2
    else:
        mx, my = n // 2, n // 2

    lay = [0 for _ in range(math.ceil(n / 2))]
    for i in range(n):
        for j in range(n):
            lay[math.floor(max(abs(i - mx), abs(j - my)))] += mat[i][j]

    print(max(lay))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](25570.png)



### 1526C1. Potions(Easy Version)

greedy, dp, data structures, brute force, *1500, https://codeforces.com/problemset/problem/1526/C1

思路：

一开始没想到用优先队列，看了题解才想到

代码：

```python
import heapq

if __name__ == "__main__":
    n = int(input())
    potions = list(map(int, input().split()))
    health = 0
    heap = []

    for potion in potions:
        health += potion
        heapq.heappush(heap, potion)
        if health < 0:
            if heap:
                health -= heap[0]
                heapq.heappop(heap)

    print(len(heap))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](1526C1.png)



### 22067: 快速堆猪

辅助栈，http://cs101.openjudge.cn/practice/22067/

思路：

思路完全一样，打包成类是有什么特殊功效吗……为什么不打包就会TLE

代码：

```python
#AC
import sys

class MinStack:
    def __init__(self):
        self.pigs = []
        self.min_pigs = []

    def push(self, x):
        self.pigs.append(x)
        if not self.min_pigs or x <= self.min_pigs[-1]:
            self.min_pigs.append(x)

    def pop(self):
        if self.pigs:
            top = self.pigs.pop()
            if top == self.min_pigs[-1]:
                self.min_pigs.pop()

    def min(self):
        if self.min_pigs:
            return self.min_pigs[-1]
        else:
            return None

min_stack = MinStack()

if __name__ == '__main__':
    commands = sys.stdin.read().split('\n')
    for command in commands:
        if command.startswith('push'):
            value = int(command.split()[1])
            min_stack.push(value)
        elif command.startswith('pop'):
            min_stack.pop()
        elif command.startswith('min'):
            min_value = min_stack.min()
            if min_value is not None:
                print(min_value)


#TLE
import sys

if __name__ == '__main__':
    orders = sys.stdin.read().split('\n')

    pig_heap = []
    pig_min = []

    for order in orders:
        order = order.strip()
        if order == 'pop':
            if pig_heap:
                pig_pop = pig_heap.pop()
                if pig_pop == pig_min[-1]:
                    pig_min.pop()
        elif order == 'min':
            if pig_heap:
                print(min(pig_heap))
        else:
            n_pig = int(order[5:])
            pig_heap.append(n_pig)
            if not pig_min or n_pig <= pig_min[-1]:
                pig_min.append(n_pig)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](22067.png)



### 20106: 走山路

Dijkstra, http://cs101.openjudge.cn/practice/20106/

思路：

学了一下Dijkstra……我怎么记得这好像是一个实现方式很简洁的算法

另外我至今没有看出下面那个代码为什么会RE

代码：

```python
#AC
import heapq

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def is_valid(x, y, m, n, mapp):
    return 0 <= x < m and 0 <= y < n and mapp[x][y] != '#'

def dijkstra(sx, sy, ex, ey, mapp, m, n):
    dist = {(sx, sy): 0}
    heap = [(0, sx, sy)]

    while heap:
        fitness, x_cur, y_cur = heapq.heappop(heap)

        if x_cur == ex and y_cur == ey:
            return fitness

        for dx, dy in d:
            nx, ny = x_cur + dx, y_cur + dy

            if is_valid(nx, ny, m, n, mapp) and mapp[nx][ny].isdigit() and mapp[x_cur][y_cur].isdigit():
                n_fitness = fitness + abs(int(mapp[nx][ny]) - int(mapp[x_cur][y_cur]))

                if (nx, ny) not in dist or dist[(nx, ny)] > n_fitness:
                    dist[(nx, ny)] = n_fitness
                    heapq.heappush(heap, (n_fitness, nx, ny))

    return 'NO'

def main():
    m, n, p = map(int, input().split())

    mapp = []
    for _ in range(m):
        mapp.append(list(input().split()))

    for _ in range(p):
        sx, sy, ex, ey = map(int, input().split())
        if not is_valid(sx, sy, m, n, mapp) or not is_valid(ex, ey, m, n, mapp):
            print('NO')
            continue

        print(dijkstra(sx, sy, ex, ey, mapp, m, n))


if __name__ == '__main__':
    main()
    

#RE
import heapq

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

def is_valid(x, y, m, n, mapp):
    return 0 <= x < m and 0 <= y < n and mapp[x][y] != '#'

def dijkstra(sx, sy, ex, ey, mapp, m, n):
    dist = {(sx, sy): 0}
    heap = [(0, sx, sy)]

    while heap:
        fitness, x_cur, y_cur = heapq.heappop(heap)

        if x_cur == ex and y_cur == ey:
            return fitness

        for dx, dy in d:
            nx, ny = x_cur + dx, y_cur + dy

            if is_valid(nx, ny, m, n, mapp) and mapp[nx][ny].isdigit() and mapp[x_cur][y_cur].isdigit():
                n_fitness = fitness + abs(int(mapp[nx][ny]) - int(mapp[x_cur][y_cur]))

                if (nx, ny) not in dist or dist[(nx, ny)] > n_fitness:
                    dist[(nx, ny)] = n_fitness
                    heapq.heappush(heap, (n_fitness, nx, ny))

    return 'NO'

def main():
    m, n, p = map(int, input().split())

    for _ in range(p):
        mapp = []
        for i in range(m):
            mapp.append(list(input().strip()))

        for __ in range(n):
            sx, sy, ex, ey = map(int, input().split())
            if not is_valid(sx, sy, m, n, mapp) or not is_valid(ex, ey, m, n, mapp):
                print('NO')
                continue

            print(dijkstra(sx, sy, ex, ey, mapp, m, n))

if __name__ == '__main__':
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](20106.png)



### 04129: 变换的迷宫

bfs, http://cs101.openjudge.cn/practice/04129/

思路：

这题做了好久，用集合存储TLE

核心就是在于可以掉头或者在附近闲逛等着石头消失

看了答案才知道用三维数组存储

没有其他方法吗

代码：

```python
import heapq

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
INF = float('inf')


def is_valid(x, y, t, mapp, r, c, k):
    if (t + 1) % k == 0:
        return 0 <= x < r and 0 <= y < c
    else:
        return 0 <= x < r and 0 <= y < c and mapp[x][y] != '#'


def bfs(sx, sy, mapp, r, c, k):
    q = [(0, sx, sy)]
    visited = [[[False] * c for _ in range(r)] for _ in range(k)]

    while q:
        t, x_cur, y_cur = heapq.heappop(q)
        if mapp[x_cur][y_cur] == 'E':
            return t

        for dx, dy in d:
            nx, ny = x_cur + dx, y_cur + dy
            nt = t + 1

            if is_valid(nx, ny, t, mapp, r, c, k) and not visited[nt % k][nx][ny]:
                heapq.heappush(q, (nt, nx, ny))
                visited[nt % k][nx][ny] = True

    return 'Oop!'


def main():
    t = int(input())
    for _ in range(t):
        r, c, k = map(int, input().split())
        mapp = []
        for i in range(r):
            mapp.append(list(input()))
            for j in range(c):
                if mapp[i][j] == 'S':
                    sx, sy = i, j

        print(bfs(sx, sy, mapp, r, c, k))

if __name__ == "__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](04129.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

wc快要机考了……脑子还一片空白，笔试也没复习

感觉这次的作业优先队列存在感相当高，学习了一下确实好用

题面一旦复杂就涉及到很多细节的处理，所以脑子还是要清醒



