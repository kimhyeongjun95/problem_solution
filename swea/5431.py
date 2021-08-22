t = int(input())

for i in range(1, t+1):

    all_students, some_students = map(int, input().split())
    k = list(map(int, input().split()))
    
    numbers = list(range(1, all_students+1))
    
    for x in k:
        if x in numbers:
            numbers.remove(x)
    
    result = ''
    for x in numbers:
        result += str(x) + ' '
    
    print(f'#{i} {result}')