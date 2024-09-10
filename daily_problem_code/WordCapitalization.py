word = list(input())
word[0] = word[0].upper()
ans = ''
for i in range(len(word)):
    ans += word[i]
print(ans)