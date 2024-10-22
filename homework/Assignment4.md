# Assignment #4: T-primes + 贪心

2024 fall, Complied by <mark>唐晨宇 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



代码

```python
n, m = map(int, input().split())
price = list(map(int, input().split()))
price.sort(reverse=False)

for i in range(n):
    if price[i] > 0 or i >= m:
        break
    profit += price[i]

print(profit)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/34B.png)



### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A



代码

```python
n = int(input())
coin = list(map(int, input().split()))
coin.sort(reverse=True)

value = 0
for i in range(n):
    if value <= 0.5 * sum(coin):
        value += coin[i]
    else:
        print(i)
        break

```



代码运行截图  <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/160A.png)



### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B



代码

```python
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(min(n * min(b) + sum(a), n * min(a) + sum(b)))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/1879B.png)



### 158B. Taxi

*special problem, greedy, implementation, 1100, https://codeforces.com/problemset/problem/158/B

思路：

这道题就是装箱子的低配版，只需要得出一个很简单的数学公式就可以解决

代码

```python
from collections import Counter

n = int(input())
s = Counter(list(map(int, input().split())))

taxi = s[4] + s[3] + (s[2] + 1) // 2

if s[3] + 2 * (s[2] % 2) < s[1]:
    taxi += (s[1] - s[3] - 2 * (s[2] % 2) + 3) // 4

print(taxi)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/158B.png)



### *230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B

思路：

判断质数用到了欧拉筛和埃氏筛



代码

Euler Sieve, 1124ms

```python
import math


def euler_sieve_prime_check(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    primes = []

    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p > n:
                break
            is_prime[i * p] = False
            if i % p == 0:
                break

    return is_prime


def CheckTPrime(x):
    sqrt_x = int(math.sqrt(x))
    if sqrt_x ** 2 == x:
        if is_prime[sqrt_x]:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'


n = input()
sample = list(map(int, input().split()))

is_prime = euler_sieve_prime_check(1000000)

for i in sample:
    print(CheckTPrime(i))

```

Eratosthenes Sieve, 998ms

```python
import math
 
def era_sieve():
 
    is_prime = [1] * (10**6)
    t_prime = set()
 
    for i in range(2, 10**6):
        if is_prime[i]:
            t_prime.add(i ** 2)
            for j in range(i * i, 10**6, i):
                is_prime[j] = 0
 
    return t_prime
 
t_prime = era_sieve()
 
input()
for i in map(int, input().split()):
    print(['NO', 'YES'][i in t_prime])
 
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/230B(euler_seive).png)

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/230B(era_sieve).png)

### *12559: 最大最小整数 （选做）

greedy, strings, sortings, http://cs101.openjudge.cn/practice/12559

思路：

难点在于比较不同位数数字的优先级

以下代码中使用的方法为构造对应的同字节数字：当比较两个不同位数的数字时，应从左往右比较（先高位后低位），若位数较小数比完一轮相等时，应当比较位数较大数的下一位与位数较小数的第一位，即位数较小数从头开始比较，按照此顺序排序即可。

代码

```python
n = int(input())
dig = list(input().split())

max_len = 0

for digit in dig:
    max_len = max(max_len, len(digit))

dig.sort(key=lambda x:int(x * (max_len // len(x)) + x[:max_len % len(x)]))

min_num = ''
max_num = ''
for i in range(n):
    min_num += dig[i]
    max_num = dig[i] + max_num

print(max_num, min_num)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/12559.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

之前研究排队那几天没做每日选做，交Assign#3的后一天补上了>_<

但是晴问还是崩，有一道好像没做

greedy对归纳能力的要求挺高的，有时候题做着做着就做成DP、bisect或者线段树的题了，但是想清楚它又不难；反而更难的是优化，就会涉及到更高级的内置函数包或者算法

老师的课件好多啊qaq，我还没看完Week5



