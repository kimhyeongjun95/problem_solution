# 백준 1806 부분합

# N 길이의 수열
# 수열에서 연속된 수들의 부분합 중
# 그 합이 S이상이 되는 것 중 가장 짧은 것의 길이

# 1. count < s: 2포인터 오른쪽 이동하며 +=
# 2. count >= s: 1포인터 오른쪽 이동하며 -=
# 2-1. 길이 갱신

n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

def find():
    result = 100001
    length = 0
    count = 0
    j = 0
    flag = False

    for i in range(n):
        # 1
        while count < s:
            if j > n-1:
                flag = True
                break
            count += arr[j]
            j += 1
            length += 1

        if flag:
            break
        
        # 2
        if count >= s:
            # 2-1
            result = min(result, length)
            count -= arr[i]
            length -= 1
            
    if result > 100000:
        return 0
    return result

answer = find()
print(answer)