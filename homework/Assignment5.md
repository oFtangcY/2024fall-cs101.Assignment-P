# Assignment #5: Greedy穷举Implementation

Updated 1939 GMT+8 Oct 21, 2024

2024 fall, Complied by <mark>唐晨宇 物理学院</mark>



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### 04148: 生理周期

brute force, http://cs101.openjudge.cn/practice/04148

思路：

中国剩余定理

代码：

```python
s = 0

while True:
    s += 1
    p, e, i, d = map(int, input().split())
    if p == -1 and e == -1 and i == -1 and d == -1:
        break
    p %= 23
    e %= 28
    i %= 33
    days_offset = (6 * p * 28 * 33 + 19 * e * 23 * 33 + 2 * i * 23 * 28 - d) % 21252
    if days_offset == 0:
        days_offset = 21252

    print('Case {}: the next triple peak occurs in {} days.'.format(s, days_offset))
    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](04148.png)



### 18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/practice/18211

代码：

```python
money = int(input())
weapon_tot = sorted(list(map(int, input().split())))

n = len(weapon_tot)
weapon_more = 0
to_sell, to_used = n - 1, 0

while to_used <= to_sell:
    if money >= weapon_tot[to_used]:
        money -= weapon_tot[to_used]
        weapon_more += 1
        to_used += 1
    else:
        if to_used == to_sell:
            break

        money += weapon_tot[to_sell]
        to_sell -= 1
        weapon_more -= 1

        if weapon_more < 0:
            weapon_more = 0
            break

print(weapon_more)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](18211.png)



### 21554: 排队做实验

greedy, http://cs101.openjudge.cn/practice/21554

思路：

链接排序的思想，在很多greedy的题中都有应用

代码：

```python
n = int(input())
t = list(map(int, input().split()))

t_i = zip(list(range(1, n + 1)), t)
t_i = sorted(t_i, key=lambda x:x[1])
row, t = zip(*t_i)

print(' '.join(map(str, row)))

avr_t = 0
for i in range(n):
    avr_t += t[i]*(n - i - 1)
avr_t /= n

print('{:.2f}'.format(avr_t))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](21554.png)



### 01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/

思路：

注意细节，在涉及到整除、求余进位时要尤其小心

代码：

```python
months = list(range(19))
Haab_months_name = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
Haab_months = dict(zip(Haab_months_name, months))

months = list(range(1, 20))
months.append(0)
Tzolkin_months_name = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
Tzolkin_months = dict(zip(months, Tzolkin_months_name))

n = int(input())

result = []
for _ in range(n):
    a, b, c = input().split()
    Haab_day = int(a[:-1]) + 1
    Haab_month = Haab_months[b]
    Haab_year = int(c)

    tot_days = 365*Haab_year + 20*Haab_month + Haab_day

    Tzolkin_year = str((tot_days - 1) // 260)
    Tzolkin_month_name = Tzolkin_months[tot_days % 20]
    Tzolkin_month_num = str(tot_days % 13)
    if Tzolkin_month_num == '0':
        Tzolkin_month_num = '13'

    result.append(Tzolkin_month_num + ' ' + Tzolkin_month_name + ' ' + Tzolkin_year)

print(n)
print('\n'.join(result))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](01008.png)



### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C

思路：

一个非常标准的贪心问题

代码：

```python
n = int(input())

x = []
h = []
for _ in range(n):
    x_i, h_i = map(int, input().split())
    x.append(x_i)
    h.append(h_i)

if n == 1:
    print(1)
    exit()

fallen_tree = 2
for i in range(1, n - 1):
    if x[i] - x[i - 1] > h[i]:
        fallen_tree += 1
    elif x[i + 1] - x[i] > h[i]:
        fallen_tree += 1
        x[i] += h[i]

print(fallen_tree)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](545C.png)



### 01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/

思路：

区间问题（第三类？）

代码：

```python
import math


def findRadar(islands, n, d):
    radar_pos_range = []
    for x, y in islands:
        if y > d:
            return -1
        radar_pos_range.append([x - math.sqrt(d**2 - y**2), x + math.sqrt(d**2 - y**2)])

    radar_pos_range.sort(key=lambda x:x[0])
    ed = radar_pos_range[0][1]
    radar = 1
    for i in range(n):
        if radar_pos_range[i][0] <= ed:
            ed = min(ed, radar_pos_range[i][1])
            continue
        else:
            radar += 1
            ed = radar_pos_range[i][1]

    return radar

case = 0
while True:
    case += 1
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        exit()
    islands = []
    for _ in range(n):
        islands.append(list(map(int, input().split())))

    radar = findRadar(islands, n, d)
    print(f'Case {case}: {radar}')
    input()
    
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![](01328.png)



## 2. 学习总结和收获

<mark>如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。</mark>

每日选做这两天的题目明显比较难，基本上都不能一次过，要花半小时甚至更多时间来完成

主要还是要捋清代码的表述. 这几天的题思路基本都没问题，问题出在把思路转化为代码的过程中怎样表述最准确、最清晰、时间复杂度最低，这方面有待加强（还得练）

作为一个只有python语法基础知识的学生来说，高级算法和变量类型还要继续学习

期中季确实比较忙，冒出了一堆ddl，争取每日选做跟上吧



