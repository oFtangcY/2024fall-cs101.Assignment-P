keyboard_layout = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9),
    'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8), ';': (1, 9),
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4), 'n': (2, 5), 'm': (2, 6), ',': (2, 7), '.': (2, 8), '/': (2, 9)
}
direct = input()
if direct == 'R':
    shift_len = -1
else:
    shift_len = 1
string = input()
for i in string:
    position = keyboard_layout.get(i)
    correct_position = tuple([position[0], position[1] + shift_len])
    for key, value in keyboard_layout.items():
        if value == correct_position:
            correct_str = key
    print(correct_str, end='')