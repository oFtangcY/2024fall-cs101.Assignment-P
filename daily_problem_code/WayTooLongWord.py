def checkLen(word):
    return len(word) > 10

n = int(input())

for _ in range(n):
    word = input()
    if checkLen(word):
        print(word[0] + str(len(word) - 2) + word[-1])
    else:
        print(word)