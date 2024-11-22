import math

N = int(input())

for a in range(6, N + 1):
    a_cubed = a**3
    for b in range(2, a):
        b_cubed = b**3
        for c in range(b, a):
            c_cubed = c**3
            for d in range(c, a):
                d_cubed = d**3
                if a_cubed == b_cubed + c_cubed + d_cubed:
                    print(f'Cube = {a}, Triple = ({b},{c},{d})')
