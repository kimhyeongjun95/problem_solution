t = int(input())


for _ in range(t):
    temp = []
    s = list(input().split(' '))
    for i in s:
        temp.append(i[::-1])

    print(' '.join(temp))