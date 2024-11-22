months = list(range(19))
Haab_months_name = ['pop', 'no', 'zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax', 'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
Haab_months = dict(zip(Haab_months_name, months))

months = list(range(1, 20))
months.append(0)
Tzolkin_months_name = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
Tzolkin_months = dict(zip(months, Tzolkin_months_name))

n = int(input())

result = []
for _ in range(n):
    a, b, c = input().split()
    Haab_day = int(a[:-1]) + 1
    Haab_month = Haab_months[b]
    Haab_year = int(c)

    tot_days = 365*Haab_year + 20*Haab_month + Haab_day

    Tzolkin_year = str((tot_days - 1) // 260)
    Tzolkin_month_name = Tzolkin_months[tot_days % 20]
    Tzolkin_month_num = str(tot_days % 13)
    if Tzolkin_month_num == '0':
        Tzolkin_month_num = '13'

    result.append(Tzolkin_month_num + ' ' + Tzolkin_month_name + ' ' + Tzolkin_year)

print(n)
print('\n'.join(result))