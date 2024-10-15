# Assign #3: Oct Mock Exam暨选做题目满百

2024 fall, Complied by 唐晨宇 物理学院



**说明：**

1）Oct⽉考： ==AC5== 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。

2）请把每个题目解题思路（可选），源码Python, 或者C++/C（已经在Codeforces/Openjudge上AC），截图（包含Accepted, 学号），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

3）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、作业评论有md或者doc。

4）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### E28674:《黑神话：悟空》之加密

http://cs101.openjudge.cn/practice/28674/

思路：

利用AscII码可以很快完成字母与数字序号的对应

代码

```python
k = int(input())
ciphertext = input()

plaintext = ''

for i in ciphertext:
    if ord(i) >= 97:
        plaintext += chr(97 + ((ord(i) - 97 - k) % 26))
    else:
        plaintext += chr(65 + ((ord(i) - 65 - k) % 26))

print(plaintext)

```

代码运行截图 ==（至少包含有"Accepted"）==

![E28674](E28674.png)



### E28691: 字符串中的整数求和

http://cs101.openjudge.cn/practice/28691/

代码

```python
a, b = input().split()
print(int(a[0:2]) + int(b[0:2]))

```

代码运行截图 ==（至少包含有"Accepted"）==

![E28691](E28691.png)



### M28664: 验证身份证号

http://cs101.openjudge.cn/practice/28664/

思路：

直接计算比较（结果与相应校验码字符的对应关系可以直接转变为列表索引与元素的链接）

代码

```python
calculate_num = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
code = ['1','0','X','9','8','7','6','5','4','3','2']

def calculateLastDig(idNum):
    sum = 0
    for i in range(0, 17):
        sum += int(idNum[i]) * calculate_num[i]
    legal_code = code[sum % 11]

    return legal_code

def CheckCode(legal_code, idNum):
    if idNum[-1] == legal_code:
        print('YES')
    else:
        print('NO')

n = int(input())

for _ in range(n):
    idNum = input()
    CheckCode(calculateLastDig(idNum), idNum)
    
```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![M28664](M28664.png)



### M28678: 角谷猜想

http://cs101.openjudge.cn/practice/28678/

思路：

这道题在每日选做中出现过

代码

```python
n = int(input())

while n != 1:
    if n % 2 == 1:
        print(f'{n}*3+1={n*3+1}')
        n = n*3+1
    else:
        print(f'{n}/2={n//2}')
        n //= 2

print('End')

```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![M28678](M28678.png)



### M28700: 罗马数字与整数的转换

http://cs101.openjudge.cn/practice/28700/

思路：

罗马数字的表示规律非常简单：

”一位“可由一个字母或两个字母组成，表示能表出的最大数字

那么只需要对每一“位”罗马数字进行数字-字符转换即可，用字典可以很方便的完成这一操作

代码

```python
 Character_Value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900} #罗马数字可能的“位”
Value_Character = dict(zip(Character_Value.values(), Character_Value.keys()))

def RomanToNum(item):
    i = 0
    num = 0
    while i < len(item):
        if i == len(item) - 1:
            num += Character_Value[item[i]]
            break
        if Character_Value[item[i + 1]] > Character_Value[item[i]]:
            num += Character_Value[item[i] + item[i + 1]]
            i += 2
        else:
            num += Character_Value[item[i]]
            i += 1

    return num

def NumToRoman(item):
    n = int(item)
    roman = ''
    for i in sorted(Value_Character.keys(), reverse=True):
        roman += Value_Character[i] * (n // i)
        n %= i

    return roman

item = input()

if item[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
    print(NumToRoman(item))
else:
    print(RomanToNum(item))

```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![M28700](M28700.png)



### *T25353: 排队 （选做）

http://cs101.openjudge.cn/practice/25353/

思路：

寻找自由变量后将自由变量从原数列中取出，在新数列中继续寻找自由变量，反复即可排出最优顺序

代码

$O(n^2)$：

```python
N, D = map(int, input().split())
h = [int(input()) for _ in range(N)]
check = [0] * len(h)
INF = 3e9

for _ in range(N):
    highwall, lowwall = -INF, INF
    idx, val = 0, INF
    for i in range(N):
        if check[i]:
            continue

        highwall = max(h[i], highwall)
        lowwall = min(h[i], lowwall)

        if h[i] + D >= highwall and h[i] - D <= lowwall and h[i] < val:
            val = h[i]
            idx = i
    check[idx] = 1
    print(h[idx])

```

优化：

```python
N, D = map(int, input().split())
h = [int(input()) for _ in range(N)]
check = [0] * len(h)
height = []
INF = 3e9

while 0 in check:
    highwall, lowwall = -INF, INF
    buffer = []
    for i in range(N):
        if check[i]:
            continue

        highwall = max(h[i], highwall)
        lowwall = min(h[i], lowwall)


        if h[i] + D >= highwall and h[i] - D <= lowwall:
            check[i] = 1
            buffer.append(h[i])

    buffer.sort()
    print(*buffer, sep='\n')


```

代码运行截图 ==（AC代码截图，至少包含有"Accepted"）==

![T25353](T25353.png)



## 2. 学习总结和收获

==如果作业题目简单，有否额外练习题目，比如：OJ“计概2024fall每日选做”、CF、LeetCode、洛谷等网站题目。==

主要时间还是放在了研究排队上面，希望老师更加仔细地讲一下关于程序的时间复杂度相关内容

贪心、双指针的具体实现方法多变，难在找出策略；而线段树等数据类型难在具体应用

直接学习这些算法的理论部分确实比较难理解，还是得在实际程序的编写过程中学











