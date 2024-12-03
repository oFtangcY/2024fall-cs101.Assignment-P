from collections import deque

d = [(1, 0), (0, -1), (-1, 0), (0, 1)]
INF = float('inf')

def is_valid(x, y, w, h):
    return 0 <= x < h + 2 and 0 <= y < w + 2


def bfs(sx, sy, ex, ey, cards, w, h):
    seg = INF
    q = deque()
    q.append((sx, sy, 0, 0, 0))
    inq = {((sx, sy), (0, 0))}

    while q:
        x_cur, y_cur, x_move, y_move, step = q.popleft()

        for dx, dy in d:
            nx, ny = x_cur + dx, y_cur + dy
            if nx == ex and ny == ey:
                if dx == x_move and dy == y_move:
                    seg = min(seg, step)
                else:
                    seg = min(seg, step + 1)
                continue

            if is_valid(nx, ny, w, h) and cards[nx][ny] == ' ' and ((nx, ny), (dx, dy)) not in inq:
                inq.add(((nx, ny), (dx, dy)))
                if dx == x_move and dy == y_move:
                    q.append((nx, ny, dx, dy, step))
                else:
                    q.append((nx, ny, dx, dy, step + 1))

    if seg == INF:
        return 'impossible'
    else:
        return f'{seg} segments'
    
def main():
    board = 0
    while True:
        board += 1
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        cards = [[' ']*(w + 2)]
        for _ in range(h):
            cards.append([' '] + list(input()) + [' '])
        cards.append([' ']*(w + 2))

        print(f'Board #{board}:')
        pair = 0
        while True:
            pair += 1
            x1, y1, x2, y2 = map(int, input().split())
            if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
                break

            print(f'Pair {pair}: ' + bfs(y1, x1, y2, x2, cards, w, h) + '.')
        print()


if __name__ == "__main__":
    main()