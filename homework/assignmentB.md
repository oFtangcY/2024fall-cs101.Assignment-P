# Assignment #B: Dec Mock Exam大雪前一天

Updated 1649 GMT+8 Dec 5, 2024

2024 fall, Complied by <mark>唐晨宇 物理学院</mark>



**说明：**

1）⽉考： AC1 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E22548: 机智的股民老张

http://cs101.openjudge.cn/practice/22548/

思路：

唯一AC题目，一个比较模式化的dp题

记录在当前日抛售获得的利润，更新最低购入价格和最高利润即可

代码：

```python
if __name__ == "__main__":
    a = list(map(int, input().split()))
    n = len(a)
    price_in = a[0]
    price_out = a[0]
    prefix = 0

    dp = [0 for _ in range(n)]
    for i in range(1, n):
        dp[i] = a[i] - price_in
        prefix = max(prefix, dp[i])
        if a[i] < price_in:
            price_in = a[i]

    print(prefix)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/22548.png)



### M28701: 炸鸡排

greedy, http://cs101.openjudge.cn/practice/28701/

思路：

考完试之后听cyk一顿分析茅塞顿开

想到了是一个递归寻求最优的办法，但当时没有立刻想到最优解是总时间除以k

代码：

```python
def fry(t, k):
    maxt = sum(t) / k
    if t[0] > maxt:
        maxt = fry(t[1:], k - 1)

    return maxt

if __name__ == "__main__":
    n, k = map(int, input().split())
    t = sorted(list(map(int, input().split())), reverse=True)

    maxt = fry(t, k)
    print('{:.3f}'.format(maxt))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/28701.png)



### M20744: 土豪购物

dp, http://cs101.openjudge.cn/practice/20744/

思路：

关键难点在于可以舍弃一件商品，开两个最优数组这个方法好巧妙

不然就和第一题那个股票没什么区别

代码：

```python
if __name__ == "__main__":
    val = list(map(int, input().split(',')))
    n = len(val)

    price, price_throw = val[0], val[0]
    ans = 0
    for i in range(1, n):
        price, price_throw = max(price + val[i], val[i]), max(price, price_throw + val[i])
        ans = max(ans, price_throw)

    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/20744.png)



### T25561: 2022决战双十一

brute force, dfs, http://cs101.openjudge.cn/practice/25561/

思路：

考试的时候都没看这道题>_<

考完后写了二十分钟写完了……虽然用测试数据debug了一下，发现是我愚蠢了，基本架构没有问题

果然在省钱的赛道上我是一马平川，在如何多花钱的问题（土豪）上我是做不了一点

代码：

```python
INF = float('inf')
tot_price = INF

def dfs(price: list, coupon: list, item, buy: list, m, n):
    global tot_price
    if item == n:
        buy_past_coupon = buy[:]
        for p in range(m):
            for q, x in coupon[p]:
                if buy[p] >= q:
                    buy_past_coupon[p] = min(buy_past_coupon[p], buy[p] - x)

        tot_price = min(tot_price, sum(buy_past_coupon) - 50 * (sum(buy) // 300))

        return

    for p in range(m):
        if price[item][p] == -1:
            continue

        buy[p] += price[item][p]
        dfs(price, coupon, item + 1, buy, m ,n)
        buy[p] -= price[item][p]


def main():
    n, m = map(int, input().split())
    price = [[-1] * m for _ in range(n)]
    for item in range(n):
        for si_i in input().split():
            si, i = map(int, si_i.split(':'))
            price[item][si - 1] = i

    coupon = [[] for _ in range(m)]
    for i in range(m):
        for q_x in input().split():
            q, x = map(int, q_x.split('-'))
            coupon[i].append((q, x))

    buy = [0] * m
    dfs(price, coupon, 0, buy, m, n)
    print(tot_price)

if __name__ == "__main__":
    main()
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/25561.png)



### T20741: 两座孤岛最短距离

dfs, bfs, http://cs101.openjudge.cn/practice/20741/

思路：

先bfs找出两个岛，然后遍历找最短的桥

可能是因为测试数据比较小所以能过，耗时还挺高的

代码：

```python
from collections import deque

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def find(mapp, island, n):
    i, j = 1, 1
    while mapp[i][j] == 0 or (mapp[i][j] == 1 and (i, j) in island):
        if j == n:
            i, j = i + 1, 1
        else:
            j += 1

    return i, j


def is_valid(x, y, n):
    return 1 <= x <= n and 1 <= y <= n

def bfs(mapp, sx, sy, n):
    q = deque()
    q.append((sx, sy))
    inq = {(sx, sy)}

    while q:
        x_cur, y_cur = q.popleft()
        for dx, dy in d:
            nx, ny = x_cur + dx, y_cur + dy
            if is_valid(nx, ny, n) and mapp[nx][ny] == 1 and (nx, ny) not in inq:
                q.append((nx, ny))
                inq.add((nx, ny))

    return inq


def bridge(island_1, island_2):
    bridge_len = float('inf')
    for x_1, y_1 in island_1:
        for x_2, y_2 in island_2:
            bridge_len = min(bridge_len, abs(x_1 - x_2) + abs(y_1 - y_2) - 1)

    return bridge_len


def main():
    n = int(input())
    mapp = [[0] * (n + 2)]
    for _ in range(n):
        mapp.append([0] + list(map(int, list(input()))) + [0])
    mapp.append([0] * (n + 2))

    sx, sy = find(mapp, {}, n)
    island_1 = bfs(mapp, sx, sy, n)

    sx, sy = find(mapp, island_1, n)
    island_2 = bfs(mapp, sx, sy, n)

    print(bridge(island_1, island_2))


if __name__ == "__main__":
    main()
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/20741.png)



### T28776: 国王游戏

greedy, http://cs101.openjudge.cn/practice/28776

思路：

听完cyk一顿输出……又是一道题面都没看的题，没想到这么简单

但是其实那个问题挺绕的，不能去纠结“哪个大臣获得奖赏最多”，应该关注“这样排你一定有比我获得奖赏多的人，如果我是我们这个排法中获得奖赏最多的人，那我的排法就优于你”

代码：

```python
from math import prod

n = int(input())
king_l, king_r = map(int, input().split())
l, r = [], []
max_pro = 0
for _ in range(n):
    a, b = map(int, input().split())
    max_pro = max(a * b, max_pro)
    l.append(a)
    r.append(b)

pro = prod(l + [king_l])
print(pro // max_pro)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/28776.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

远离oi从我做起……

按照这个月考来说期末考试或许是要寄了

急了，得复习一下机考了，要不然要挂科了



