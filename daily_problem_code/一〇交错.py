S = input()

length = 1
len_max = 0
for i in range(1, len(S)):
    if S[i - 1] == S[i]:
        if length > len_max:
            len_max = length
        length = 1
    else:
        length += 1

if length > len_max:
    len_max = length

print(len_max)