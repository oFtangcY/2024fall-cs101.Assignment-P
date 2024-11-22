import math


def findRadar(islands, n, d):
    radar_pos_range = []
    for x, y in islands:
        if y > d:
            return -1
        radar_pos_range.append([x - math.sqrt(d**2 - y**2), x + math.sqrt(d**2 - y**2)])

    radar_pos_range.sort(key=lambda x:x[0])
    ed = radar_pos_range[0][1]
    radar = 1
    for i in range(n):
        if radar_pos_range[i][0] <= ed:
            ed = min(ed, radar_pos_range[i][1])
            continue
        else:
            radar += 1
            ed = radar_pos_range[i][1]

    return radar

case = 0
while True:
    case += 1
    n, d = map(int, input().split())
    if n == 0 and d == 0:
        exit()
    islands = []
    for _ in range(n):
        islands.append(list(map(int, input().split())))

    radar = findRadar(islands, n, d)
    print(f'Case {case}: {radar}')
    input()