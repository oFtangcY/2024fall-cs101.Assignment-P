def pell():
    PellSequence = [0] * (10**6 + 1)
    PellSequence[1] = 1
    PellSequence[2] = 2
    for i in range(2, 10**6 + 1):
        PellSequence[i] = (2 * PellSequence[i - 1] + PellSequence[i - 2]) % 32767

    return PellSequence

n = int(input())

PellSequence = pell()

for i in range(n):
    print(PellSequence[int(input())])