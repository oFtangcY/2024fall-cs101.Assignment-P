length = []
i = 0
result = []
while True:
    value = float(input())
    if value == 0:
        break
    length.append(value)
for j in length:
    length_card = 0
    k = 2
    while length_card < j:
        length_card += 1 / k
        k += 1
    result.append(k - 2)
for ans in result:
    print(str(ans) + ' card(s)')
