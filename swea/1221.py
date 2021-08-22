numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

t = int(input())

for i in range(1, t+1):
    case_symbol, case_number = input().split() 
    case = list(input().split())
    

    case = sorted(case, key=numbers)

print(case)