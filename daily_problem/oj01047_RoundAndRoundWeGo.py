from collections import Counter

while True:
    try:
        num = input()
        n = len(num)
        num_int = int(num)
        num_count = Counter(list(num))
        judge = 1

        for i in range(1, n + 1):
            s_int = num_int * i
            s = str(s_int)
            if len(s) < n:
                s = '0' * (n - len(s)) + s

            if Counter(list(s)) != num_count:
                judge = 0
                break

        print(num + ' is ' + ['not ', ''][judge] + 'cyclic')

    except EOFError:
        break

