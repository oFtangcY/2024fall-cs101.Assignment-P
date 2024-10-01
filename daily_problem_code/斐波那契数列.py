def fibonacci():
    sequence = [1, 1]
    i = 2
    while i <= 19:
        sequence.append(sequence[i - 1] + sequence[i - 2])
        i += 1
    return sequence

n = int(input())

fibonacci = fibonacci()

for _ in range(n):
    print(fibonacci[int(input()) - 1])