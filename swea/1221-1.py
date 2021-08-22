new_numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

t = int(input())

for i in range(t):
    order, test_number = input().split()
    numbers_input = list(input().split())
     
    answer = []

    for x in new_numbers:
        for j in numbers_input:
            if j == x:
                answer.append(j)

    print(order)
    print(' '.join(answer))
    