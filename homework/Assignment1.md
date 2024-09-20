### Assignment #1

##### 02733: 判断闰年

###### code

```python
a = int(input())
if a%4 == 0:
    if a%100 == 0 and a%400 != 0:
        print("N")
    else:
        print("Y")
else:
    print("N")
```

###### result: AC

![02733](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/02733.png)

##### 02750: 鸡兔同笼

###### code

```python
a = int(input())
if a%2 != 0:
    print(0,0)
else:
    n_max = int(a/2)
    if a%4 == 0:
        n_min = int(a/4)
    else:
        n_min = a//4 + 1
    print(int(n_min), int(n_max))
```

###### result: AC

![02750](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/02750.png)

##### 50A. Domino piling

###### code

```python
M, N = input().split()
M = int(M)
N = int(N)
n = M*N//2
print(n)
```

###### result: AC

![50A](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/50A.png)

##### 1A. Theatre Square

###### code

```python
import math

n, m, a = map(int, input().split())
result = int(math.ceil(n / a) * math.ceil(m / a))
print(result)
```

###### result: AC

![1A](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/1A.png)

##### 112A. Petya and Strings

###### code

```python
str1 = list(input().lower())
str2 = list(input().lower())
n = len(str1)
if str1 == str2:
    print('0')
for i in range(0, n):
    if ord(str1[i]) < ord(str2[i]):
        print('-1')
        break
    if ord(str1[i]) > ord(str2[i]):
        print('1')
        break
```

###### result: AC

![112A](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/02733.png)

##### 231A. Team

###### code

```python
n = int(input())
num = 0
att = [[] for i in range(n)]
for i in range(n):
    att[i] = list(map(int, input().split()))
    if sum(att[i]) >= 2:
        num += 1
print(num)
```

###### result: AC

![231A](https://github.com/oFtangcY/2024fall-cs101-personal/blob/main/homework/fig/02733.png)

#### 学习总结和收获

所有题我都做了——题有点简单，但打字速度要求有点高。

另外也尝试了算法基础上的题目，主要是数学思维的要求；在Codewars平台上也做了一些题目，比算法基础要难一些。
