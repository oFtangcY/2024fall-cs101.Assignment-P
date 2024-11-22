def relate_to_7(num):
    if '7' in str(num) or num % 7 == 0:
        return False
    else:
        return True

square_sum = 0
n = int(input())
for i in range(1, n + 1):
    if relate_to_7(i):
        square_sum += i**2
print(square_sum)