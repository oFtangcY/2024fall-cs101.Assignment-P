def find_cycle(n, a):
    cycle = []
    for i in range(n):
        st = i
        cir = 0
        while True:
            cir += 1
            st = a[st]
            if st == i:
                break
        cycle.append(cir)

    return cycle

def change(i, k, a):
    for j in range(k):
        i = a[i]

    return i

while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1

    while True:
        str_in = input().split(' ', 1)
        k = int(str_in[0])
        if k == 0:
            break
        encoding_mes = list(str_in[1])
        encoding_mes.extend([' ']*(n - len(encoding_mes)))
        encoded_mes = [' ']*n

        cycle = find_cycle(n, a)
        for i in range(n):
            encoded_mes[change(i, k % cycle[i], a)] = encoding_mes[i]

        print(''.join(encoded_mes))

    print()

