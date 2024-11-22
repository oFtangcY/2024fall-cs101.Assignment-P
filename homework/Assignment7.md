# Assignment #7: Nov Mock Exam立冬

Updated 1646 GMT+8 Nov 7, 2024

2024 fall, Complied by <mark>唐晨宇  物理学院</mark>



**说明：**

1）⽉考： <mark>AC6</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E07618: 病人排队

sorttings, http://cs101.openjudge.cn/practice/07618/

思路：

用了一个最简单分类排序

应该不用再优化了？

代码：

```python
old = []
young = []

n = int(input())
for _ in range(n):
    id, age = input().split()
    age = int(age)
    if age >= 60:
        old.append([id, age])
    else:
        young.append(id)

old.sort(key=lambda x:x[1], reverse=True)
for id, age in old:
    print(id)
print('\n'.join(young))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/E07618.png)



### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/practice/23555/

思路：

主要用了字典的形式来存储矩阵元（*字典可以设置默认值*）

代码：

```python
def matrices_multiply(x, y):
    product = {}
    for r in range(n):
        for c in range(n):
            product.setdefault((r, c), 0)
            for i in range(n):
                product[(r, c)] += x.get((r, i), 0)*y.get((i, c), 0)

    return product

if __name__ == '__main__':
    x = {}
    y = {}
    n, m1, m2 = map(int, input().split())
    for _ in range(m1):
        r, c, value = map(int, input().split())
        x[(r, c)] = value
    for _ in range(m2):
        r, c, value = map(int, input().split())
        y[(r, c)] = value

    product = matrices_multiply(x, y)
    for ind, value in product.items():
        if value == 0:
            continue
        print(ind[0], ind[1], value)
```



代码运行截图 ==（至少包含有"Accepted"）==

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/E23555.png)



### M18182: 打怪兽 

implementation/sortings/data structures, http://cs101.openjudge.cn/practice/18182/

思路：

结合了字典和列表的用法

字典便于查找，列表可以排序

代码：

```python
def killTheMonster(x, b, m):
    skills = sorted(list(x.items()), key=lambda x:x[0])
    for t, dec in skills:
        if len(dec) <= m:
            b -= sum(dec)
        else:
            dec.sort(reverse=True)
            b -= sum(dec[:m])
        if b <= 0:
            return t

    if b > 0:
        return 'alive'

if __name__ == '__main__':
    nCases = int(input())
    for _ in range(nCases):
        skills = {}
        n, m, b = map(int, input().split())
        for __ in range(n):
            ti, xi = map(int, input().split())
            skills[ti] = skills.get(ti, [])
            skills[ti].append(xi)
        print(killTheMonster(skills, b, m))
```



代码运行截图 <mark>（至少包含有"Accepted"）[</mark>

![](](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/)M18182.png)



### M28780: 零钱兑换3

dp, http://cs101.openjudge.cn/practice/28780/

思路：

无脑dp（好像大家的python程序AC时间都是10000ms的量级？）

代码：

```python
def match(coins, m):
    dp = [1000001]*(max(m, coins[-1]) + 7)
    for coin in coins:
        dp[coin] = 1

    for i in range(coins[0], m + 1):
        if dp[i] != 1000001:
            continue

        for coin in coins:
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[m]


if __name__ == '__main__':
    n, m = map(int, input().split())
    coinvalue = sorted(list(map(int, input().split())))

    ans = match(coinvalue, m)
    if ans == 1000001:
        print(-1)
    else:
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/M28780.png)



### T12757: 阿尔法星人翻译官

implementation, http://cs101.openjudge.cn/practice/12757

思路：

好像、据说是一个单调栈的题目？

但是我觉得在这样的题面条件下直接按输入字符串（单词）来判断反而更简单

代码：

```python
English = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
Numbers = list(list(range(21)))
Numbers.extend([i*10 for i in range(3, 10)])
EnglishNumbers = dict(zip(English, Numbers))
ans, num = 0, []

if __name__ == '__main__':

    for word in input().split():
        if word == 'negative':
            print('-', end='')
            continue
        if word == 'hundred':
            num[-1] *= 100
            continue
        if word == 'million':
            ans += num[-1]*1000000
            num = []
            continue
        if word == 'thousand':
            ans += num[-1]*1000
            num = []
            continue
        if num != []:
            num[-1] += EnglishNumbers[word]
        else:
            num.append(EnglishNumbers[word])

    if num != []:
        ans += num[-1]
    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/T12757.png)



### T16528: 充实的寒假生活

greedy/dp, cs10117 Final Exam, http://cs101.openjudge.cn/practice/16528/

思路：

十分钟内解决

一个非常典型的最多区间覆盖问题

dp好像也是类似的思路？我没有仔细想过

代码：

```python
affairs = []
ans = 1

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        affairs.append(list(map(int, input().split())))
    affairs.sort(key=lambda x:x[1])
    end = affairs[0][1]
    for l ,r in affairs[1:]:
        if l <= end:
            continue
        end = r
        ans += 1

    print(ans)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/T16528.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

每日选做之后有时间补一下

感觉这一次的月考题比上一次做的更顺一点（可能题目也并不是很难？主要几个题都相对繁琐，思路清晰就很简单）

没有考比较难的贪心、递归和dp的问题，不然就完啦qaq

字典相关函数还得熟悉一下



