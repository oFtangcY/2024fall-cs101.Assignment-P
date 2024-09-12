def reduceNum(n):
    result = []
    if n == 1:
        result = [-1]
    else:
        while n != 1:
            for i in range(2, n + 1):
                if n % i == 0:
                    result.append(i)
                    n = n // i
                    break
    return result

factor = reduceNum(int(input()))
for j in factor:
    if factor.count(j) > 1:
        print(0)
        break
    elif len(factor) % 2 == 0 or factor == [-1] :
        print(1)
        break
    else:
        print(-1)
        break
