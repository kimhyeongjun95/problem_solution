# 백준 17091 단어 시계

# 분 == 0: o' clock
# 1 <= 분 <= 30: past
# 30 < 분: to

# 1 <= h <= 12
# 0 <= m < 60

time_format = [
    '', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
    'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 
    'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one',
    'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six',
    'twenty seven', 'twenty eight', 'twenty nine'
]

def caculate(h, m, branch):
    if m == 1:
        return f'{time_format[m]} minute {branch} {time_format[h]}'
    elif m == 15 or m == 45:
        return f'quarter {branch} {time_format[h]}'
    elif 0 <= m <= 29:
        return f'{time_format[m]} minutes {branch} {time_format[h]}'
    elif m == 30:
        return f'half {branch} {time_format[h]}'

h = int(input())
m = int(input())

result = ''

if m == 0:
    result = f"{time_format[h]} o' clock"
elif 1 <= m <= 30:
    result = caculate(h, m, 'past')
else:
    if h == 12:
        h = 0
    result = caculate(h+1, 60-m, 'to')

print(result)