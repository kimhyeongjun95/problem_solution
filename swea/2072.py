t = int(input())

for tc in range(t):
    numbers = input()
    numbers = numbers.split()
    numbers = list(map(int, numbers))

    total = 0

    for number in numbers:
        if number % 2:
            total += number

    print(f'#{tc+1} {total}')