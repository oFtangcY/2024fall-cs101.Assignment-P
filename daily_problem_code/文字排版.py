n = int(input())
art = input()
result = []
while len(art) > 80:
    for i in range(80):
        if art[80 - i] == ' ':
            result.append(art[:80 - i])
            art = art[81 - i:]
            break
result.append(art)
for i in result:
    print(f"{i}")