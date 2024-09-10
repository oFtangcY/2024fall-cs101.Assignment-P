situation = input()
row = 1
for i in range(len(situation) - 1):
    if int(situation[i + 1]) == int(situation[i]):
        row += 1
    else:
        row = 1
    if row == 7:
        print('YES')
        break
if row < 7:
    print('NO')