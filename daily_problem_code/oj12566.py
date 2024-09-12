ori = input().lower()
num = 1
for i in range(len(ori) - 1):
    if ori[i + 1] == ori[i]:
        num += 1
    else:
        print(f"({ori[i]}, {num})", end='')
        num = 1
print(f"({ori[-1]}, {num})")
