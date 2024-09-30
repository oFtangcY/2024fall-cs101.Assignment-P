while True:
    N = int(input())
    if N == 0:
        break

    hotels = []
    for _ in range(N):
        D, C = map(int, input().split())
        hotels.append((D, C))

    hotels.sort()

    num_candidates = 0
    min_cost = float('inf')

    for d, c in hotels:
        if c < min_cost:
            num_candidates += 1
            min_cost = c

    print(num_candidates)
