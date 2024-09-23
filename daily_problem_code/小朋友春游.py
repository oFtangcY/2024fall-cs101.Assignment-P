n = int(input())
children = sorted(list(map(int, input().split())))
children_loss = []
for i in range(1, n + 1):
    if i not in children:
        children_loss.append(i)
    else:
        children.remove(i)

print(' '.join(map(str, children_loss)))
print(' '.join(map(str, children)))