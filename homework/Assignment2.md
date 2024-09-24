# Assignment #2: 语法练习

#### 唐晨宇  物理学院

## 1. 题目

### 263A. Beautiful Matrix

##### 代码

```python
r = 0
for i in range(5):
    c = list(map(int, input().split()))
    if sum(c) == 1:
        k = c
        r = i
for i in range(5):
    if k[i] == 1:
        print(abs(r - 2) + abs(i - 2))
```

![263A](263A-1727170649094-5.png)

### 1328A. Divisibility Problem

##### 代码

```python
# Reading number of test cases
t = int(input())

# Processing each test case
for _ in range(t):
    a, b = map(int, input().split())

    # Calculate remainder
    remainder = a % b

    if remainder == 0:
        # If a is already divisible by b
        print(0)
    else:
        # Calculate how much needs to be added
        print(b - remainder)
```

![1328A](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/1328A.png)

### 427A. Police Recruits

##### 代码

```python
n = int(input())
ans = 0
recruit = 0
event = list(map(int, input().split()))
for i in range(n):
    if event[i] > 0:
        recruit += event[i]
    elif recruit > 0:
        recruit += event[i]
    else:
        ans += 1
print(ans)
```

![427A](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/427A.png)

### 02808: 校门外的树

##### 代码

```python
L, M = map(int, input().split())
tot = set(range(L + 1))
area = set()
for i in range(M):
    b, e = map(int, input().split())
    area.update(range(b, e + 1))
print(len(tot - area))
```

![02808](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/oj02808.png)

### sy60: 水仙花数II

##### 代码

```python
a, b = map(int, input().split())
ans = []
result = []
counter = 0
for i in range(a, b + 1):
    if i == (i // 100)**3 + (i % 100 // 10)**3 + (i % 10)**3:
        result.append(str(i))
        counter += 1
if result != []:
    print(' '.join(result))

if counter == 0:
    print('NO')
```

![60](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/sy60.png)

### 01922: Ride to School

##### 代码

```python
import math

def arrive_time(v, t_0):
    t = 4.5 / v * 3600 + t_0
    return t

result = []

while True:
    n = int(input())
    if n == 0:
        break
    
    t = float('inf')
    
    for _ in range(n): 
        v, t_0 = map(int, input().split())
        if t_0 >= 0 and t > arrive_time(v, t_0):
            t = arrive_time(v, t_0)

    result.append(str(math.ceil(t)))

print('\n'.join(result))
```

![01922](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/oj01922.png)

## 2. 学习总结和收获

中秋那些800的题偷懒了没做~

以前代码敲的不多（缺少实际应用场景），学c++也和python不大一样，没太注意写代码的习惯；这段时间代码写多了才发现python程序中对函数（或者Class）的定义真好用，可以让代码写的非常简洁清晰。

python里面真的挺多细节的，光了解基础语法没啥用，还得自己写代码应用。





