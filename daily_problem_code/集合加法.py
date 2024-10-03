from collections import Counter

def calculate_pairs(arr1, arr2, target_sum):
    counter1 = Counter(arr1)
    counter2 = Counter(arr2)

    ans = 0
    for item in counter1:
        if target_sum - item in counter2:
            ans += counter1[item] * counter2[target_sum - item]

    return ans


for _ in range(int(input())):
    s = int(input())
    input()
    l1 = list(map(int, input().split()))
    input()
    l2 = list(map(int, input().split()))

    ans = calculate_pairs(l1, l2, s)
    print(ans)