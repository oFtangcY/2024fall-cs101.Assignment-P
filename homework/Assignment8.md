# Assignment #8: 田忌赛马来了

Updated 1021 GMT+8 Nov 12, 2024

2024 fall, Complied by <mark>唐晨宇  物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/practice/12558/ 

思路：

关键在于边界长度等于上下左右四块中0的个数

加保护圈常规操作

代码：

```python
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
count = 0

n, m = map(int, input().split())
imap = [[0]*(m + 2)]
for _ in range(n):
    imap.append([0] + list(map(int, input().split())) + [0])
imap.append([0]*(m + 2))

def dfs(x, y):
    global count
    imap[x][y] = -1
    for s in range(4):
        nx, ny = x + dx[s], y + dy[s]
        if 0 <= nx < n + 2 and 0 <= ny < m + 2:
            if imap[nx][ny] == 0:
                count += 1
            elif imap[nx][ny] == 1:
                dfs(nx, ny)


for i in range(1, n + 1):
    for j in range(1, m + 1):
        if imap[i][j] == 1:
            dfs(i, j)

print(count)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](12558.png)



### LeetCode54.螺旋矩阵

matrice, https://leetcode.cn/problems/spiral-matrix/

与OJ这个题目一样的 18106: 螺旋矩阵，http://cs101.openjudge.cn/practice/18106

思路：

一种新思路：给伴随visited空间加保护圈

以及判断结束的标准是visited空间中所有点都已遍历

代码：

```python
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](LC54.png)



### 04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/

思路：

字典的应用

代码：

```python
d = int(input())
n = int(input())
rubbish_distribution = {}

for _ in range(n):
    x, y, i = map(int, input().split())
    for r in range(max(0, x - d), min(1024, x + d) + 1):
        for c in range(max(0, y - d), min(1024, y + d) + 1):
            rubbish_distribution[(r, c)] = rubbish_distribution.setdefault((r, c), 0) + i

rubbish = list(rubbish_distribution.values())
max_rubbish = max(rubbish)

print(rubbish.count(max_rubbish), max_rubbish)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](04133.png)



### LeetCode376.摆动序列

greedy, dp, https://leetcode.cn/problems/wiggle-subsequence/

与OJ这个题目一样的，26976:摆动序列, http://cs101.openjudge.cn/routine/26976/

思路：

应该可以算是一个比较常规的dp题目

注意要把“有效数字”只有两个或者一个的情况单独讨论

代码：

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        if len(nums) == 2:
            if nums[0] != nums[1]:
                return 2
            else:
                return 1

        dp = [nums[0]]
        for j in range(1, len(nums)):
            if nums[j] != nums[0]:
                dp.append(nums[j])
                s = j
                break
        else:
            return 1

        d = nums[s] - nums[0]
        for i in range(s + 1, len(nums)):
            if (nums[i] - nums[i - 1])*d < 0:
                dp.append(nums[i])
                d = nums[i] - nums[i - 1]
            else:
                dp[-1] = nums[i]

        return len(dp)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](LC376.png)



### CF455A: Boredom

dp, 1500, https://codeforces.com/contest/455/problem/A

思路：

这道题做的那叫一个屡战屡败，屡败屡战

TLE，MLE，WA，RE

都经历过了……可以召唤神龙吗>_<

我现在非常像知道有什么办法可以减小这段代码的内存（GPT告诉我可以选择不建立新的nseq列表而改用索引）

另外这个代码不考虑内存限制能过吗？

确实有些情况下dp相比递归要快很多

代码：

```python
#MLE
from collections import Counter
 
point = 0
 
def delete(seq):
    if seq == []:
        return
 
    global point, count
    a_k = seq[-1]
 
    if count[a_k - 1] != 0 and (a_k + count[a_k - 1]*(a_k - 1)) > (count[a_k]*a_k + count[a_k - 2]*(a_k - 2) + a_k - 1):
        point += (a_k - 1)*count[a_k - 1]
        nseq = seq[:-count[a_k - 2] - count[a_k- 1] - count[a_k]]
        delete(nseq)
    else:
        point += a_k * count[a_k]
        nseq = seq[:-count[a_k] - count[a_k - 1]]
        count[a_k], count[a_k - 1] = 0, 0
        delete(nseq)
 
 
n = int(input())
a = sorted(list(map(int, input().split())))
count = Counter(a)
delete(a)
print(point)
```



```python
#AC
from collections import Counter


def delete(count):
    M = 100001
    dp = [[0, 0] for _ in range(M + 1)]

    for i in range(1, M + 1):
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i - 1][0] + count[i]*i

    return max(dp[M][0], dp[M][1])


n = int(input())
a = sorted(list(map(int, input().split())))
count = Counter(a)

print(delete(count))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](455A.png)



### 02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/practice/02287

思路：

二分查找不难想到

关键是要在考虑完赢的情况后在考虑平局的情况，不能同时考虑，从而追求利益最大化

哦另外我在想用数学图的思维（bipartite graph）怎么写这题的程序

用二分图着色的办法怎么实现？暂时还没想出来

代码：

```python
from bisect import bisect_left

while True:
    n = int(input())
    if n == 0:
        exit(0)
    tian = sorted(list(map(int, input().split())))
    king = sorted(list(map(int, input().split())))
    count = 0
    ties = []

    for horse in tian:
        index = bisect_left(king, horse)
        if index > 0:
            count += 1
            king.pop(index - 1)
        else:
            ties.append(horse)

    index = 0
    for horse in ties:
        if horse < king[index]:
            count -= 1
        else:
            index += 1

    print(200*count)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](02287.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

补每日选做的过程举步维艰……

感觉自己的思维在学到递归、dp、dfs之后变的有些僵化了

dp对思维灵活性的要求还是很高的

可能和题做的少也有一定的关系

争取加快进度，追一下题量



