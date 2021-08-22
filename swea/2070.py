t = int(input())

for i in range(1, t+1):
    numbers = list(map(int, input().split()))
    max_number = max(numbers)

    print(f'#{i} {max_number}')