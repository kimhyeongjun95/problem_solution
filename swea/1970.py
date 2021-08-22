coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

t = int(input())

for i in range(1, t+1):
    money = int(input())
    result = []

    for x in coins:
        count = 0

        while money >= x:
            money -= x
            count += 1

        result.append(str(count))

    print(f'#{i}')
    print(' '.join(result))