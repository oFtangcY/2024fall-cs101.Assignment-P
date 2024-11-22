import re


def FormRCtoFormA1(r, c):
    i = c
    c_letter = ''
    while i > 0:
        if i % 26 == 0:
            i = i // 26 - 1
            c_letter = 'Z' + c_letter
        else:
            c_letter = chr(64 + i % 26) + c_letter
            i = i // 26

    return (c_letter + r)

def FormA1toFormRC(r, c):
    l = len(c) - 1
    c_num = 0
    for i in range(len(c)):
        c_num += (ord(c[i]) - 64)*(26**(l - i))

    return f'R{r}C{str(c_num)}'

n = int(input())
for _ in range(n):
    coordinate = input()
    match = re.match('R(\d+)C(\d+)', coordinate)
    if match != None:
        print(FormRCtoFormA1(match.group(1), int(match.group(2))))
    else:
        match = re.match('([A-Z]+)(\d+)', coordinate)
        print(FormA1toFormRC(match.group(2), match.group(1)))