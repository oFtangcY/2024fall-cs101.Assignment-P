# Assignment #6: Recursion and DP

Updated 2201 GMT+8 Oct 29, 2024

2024 fall, Complied by <mark>同学的姓名、院系</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy119: 汉诺塔

recursion, https://sunnywhy.com/sfbj/4/3/119  

思路：

对于一个N阶问题，其次级结构即为将上方的N-1阶汉诺塔移至中间柱，将最大的盘移至目标柱后再将N-1阶结构从中间柱移至目标柱.

即step(N) = step(N - 1) + step(1) + step(N - 1).

代码：

```python
def hanoi_tower(n, a, b, c):
    if n == 1:
        return [a + '->' + b]
    else:
        return hanoi_tower(n - 1, a, c, b) + [a + '->' + b] + hanoi_tower(n - 1, c, b, a)

n = int(input())
print(2**n - 1)
print('\n'.join(hanoi_tower(n, 'A', 'C', 'B')))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/hanoi_tower.png)



### sy132: 全排列I

recursion, https://sunnywhy.com/sfbj/4/3/132

思路：

arrange函数进行递归前后的标记布尔值修改极其关键！！！

代码：

```python
result = []

def arrange(s):
    if len(s) == n:
        result.append(s)
        return

    for i in range(1, n + 1):
        if state[i]:
            continue
        else:
            state[i] = True
            arrange(s + str(i))
            state[i] = False


n = int(input())
state = [False] * (n + 1)
arrange('')

for arr in result:
    print(' '.join(arr))
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/full_arrange.png)



### 02945: 拦截导弹 

dp, http://cs101.openjudge.cn/2024fallroutine/02945

思路：

...只能说我没有想到这个思路.

最大不增子序列倒是考虑了，但是

```python
if pos < len(dp):
    dp[pos] = height
```

这句很关键.

代码：

```python
from bisect import bisect_right


def intercept(heights):
    heights.reverse()
    dp = []
    for height in heights:
        pos = bisect_right(dp, height)
        if pos < len(dp):
            dp[pos] = height
        else:
            dp.append(height)

    return len(dp)

if __name__ == '__main__':
    k = int(input())
    heights = list(map(int, input().split()))
    print(intercept(heights))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/interceppt_missiles.png)



### 23421: 小偷背包 

dp, http://cs101.openjudge.cn/practice/23421

思路：

```python
dp[j] = max(p[i] + dp[j - w[i]], dp[j])
```

这是一个dp中极其常见的结构.

代码：

```python
def choose_item(n, b, p, w):
    dp = [0 for _ in range(b + 1)]

    for i in range(n):
        for j in range(b, w[i] - 1, -1):
            dp[j] = max(p[i] + dp[j - w[i]], dp[j])
                
    return dp[b]

n, b = map(int, input().split())
price = list(map(int, input().split()))
weight = list(map(int, input().split()))

print(choose_item(n, b, price, weight))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/the_thiefs_bag.png)



### 02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/practice/02754

思路：

和全排列有一定的相似性

代码：

```python
place = []

def arrange_queen(s):
    if len(s) == 8:
        place.append(s)
        return
    else:
        for i in range(1, 9):
            if all(i != int(s[j]) and abs(len(s) - j) != abs(int(s[j]) - i) for j in range(len(s))):
                arrange_queen(s + str(i))


arrange_queen('')
n = int(input())
for _ in range(n):
    print(place[int(input()) - 1])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/eight_queens.png)



### 189A. Cut Ribbon 

brute force, dp 1300 https://codeforces.com/problemset/problem/189/A

思路：

嗯~和小偷背包就很像.

代码：

```python
dp = [-4000]*4007

def cut(n, a, b, c):
    dp[a], dp[b], dp[c] = 1, 1, 1
    for l in range(1, n + 1):
        for ll in [a, b, c]:
            if l >= ll:
                dp[l] = max(dp[l - ll] + 1, dp[l])

    return dp[n]

n, a, b, c = map(int, input().split())
print(cut(n, a, b, c))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/CutRibbon.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊~~

好难啊>_<  |?|__|?|

dp很多题都要先看答案，看完再自己想一遍过程，感觉有些时候get不到那个点qaq

期中季好忙，每日选做好久没做了~~

等我考完试恶补recursion和dp.



