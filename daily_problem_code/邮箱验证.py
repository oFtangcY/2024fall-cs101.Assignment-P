def checkAt(address):
    return address.count('@') == 1

def checkHeadAndTail(address):
    return not (address[0] in '.@' or address[-1] in '.@')

def checkAtAndDot(address):
    at_pos = address.find('@')
    return not (address[at_pos - 1] == '.' or address[at_pos + 1] == '.' or address[at_pos + 1:].count('.') == 0)


def check(address):
    return checkAt(address) and checkAtAndDot(address) and checkHeadAndTail(address)


while True:
    try:
        print('YES' if check(input()) else 'NO')
    except EOFError:
        break
