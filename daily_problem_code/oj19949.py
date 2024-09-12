N = int(input())
result = 0
for i in range(N):
    sentence = input()
    sentence_1 = sentence.replace('### ###', ' ')
    result += len(sentence_1.split('###')) // 2
print(result)
