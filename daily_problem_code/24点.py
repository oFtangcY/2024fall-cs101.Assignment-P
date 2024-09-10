def multiply(list1, list2):
    ans = []
    for i in range(len(list1)):
        ans.append(list1[i] * list2[i])
    return ans

m =int(input())
cof = [[1, 1, 1, 1],
       [-1, 1, 1, 1],
       [1, -1, 1, 1],
       [1, 1, -1, 1],
       [1, 1, 1, -1],
       [-1, -1, 1, 1],
       [-1, 1, -1, 1],
       [-1, 1, 1, -1],
       [1, -1, -1, 1],
       [1, -1, 1, -1],
       [1, 1, -1, -1],
       [-1, -1, -1, 1],
       [-1, -1, 1, -1],
       [-1, 1, -1, -1],
       [1, -1, -1, -1],
       [-1, -1, -1, -1]]
result = ['NO' for _ in range(m)]

for i in range(m):
    num = list(map(int, input().split()))
    for j in cof:
        if sum(multiply(num, j)) == 24:
            result[i] = 'YES'
            break

for ans in result:
    print(ans)