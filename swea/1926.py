# SWEA 1926 간단한 369게임

# 35|1번 36|2번

result = []
n = int(input())
for i in range(1, n+1):
    count = 0
    for j in str(i):
        if j in ['3', '6', '9']:
            count += 1
    
    if count:
        result.append('-'*count)
    else:
        result.append(str(i))
    
print(' '.join(result))