def CheckYear(y):
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            return 0
        else:
            return 1
    else:
        return 0

date_begin = input()
y = int(date_begin[0:4])
m = int(date_begin[5:7])
d = int(date_begin[-2:])
days = int(input())

DaysInMonth = [{1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}, {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}]

while days > 0:
    days_in_current_month = DaysInMonth[CheckYear(y)].get(m)
    if d < days_in_current_month:
        d += 1
    else:
        d = 1
        m += 1

    if m > 12:
        m = 1
        y += 1

    days -= 1

print(str(y) + '-' + str(m).zfill(2) + '-' + str(d).zfill(2))
