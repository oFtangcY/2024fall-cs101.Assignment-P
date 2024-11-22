# Reading number of test cases
t = int(input())

# Processing each test case
for _ in range(t):
    a, b = map(int, input().split())

    # Calculate remainder
    remainder = a % b

    if remainder == 0:
        # If a is already divisible by b
        print(0)
    else:
        # Calculate how much needs to be added
        print(b - remainder)