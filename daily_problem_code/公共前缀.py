n = int(input())
prefix = input()

for i in range(n - 1):
    i = input()
    for j in range(len([prefix, i][len(prefix) > len(i)])):
        if prefix[j] != i[j]:
            prefix = prefix[:j]
            break

print(prefix)