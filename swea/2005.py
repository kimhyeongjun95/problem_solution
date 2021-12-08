# SWEA 2005 파스칼 삼각형

t = int(input())
for tc in range(1, t+1):
    n = int(input())

    results = [[] for _ in range(n)]
    for i in range(n):
        
        for j in range(i+1):
            if j == 0 or j == i:
                results[i].append('1')
            else:
                temp = int(results[i-1][j-1]) + int(results[i-1][j])
                results[i].append(str(temp))

    print(f'#{tc}')
    for result in results:
        print(' '.join(result)) 