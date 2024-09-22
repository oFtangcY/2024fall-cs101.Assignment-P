def reverse(n):
    n_list = list(n)[2:]
    n_list.reverse()
    return n_list

n = int(input())
n_2 = bin(n)

if reverse(n_2) == list(n_2)[2:]:
    print('Yes')
else:
    print('No')
