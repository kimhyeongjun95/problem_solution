# SWEA 1216 회문2
# 가장 긴 회문의 길이를 구하는 문제

def palindrome(arr):
    ans = ''
    for i in range(100):  # 돌아가는 갯수 늘리기
        for j in range(i+1):  # 탐색 위치 바꾸기
            for k in range(100): # 한줄씩 바꾸기
                flag = True

                M = 100 - i
                #가로
                for idx1 in range(M // 2): # 앞뒤 비교하는것
                    start = i + idx1
                    end = i + M - 1 - idx1
                    if arr[k][start] != arr[k][end]:
                        flag = False
                        break
                if flag:
                    return len(arr[r][i:i + M])
                #세로
                flag = True
                for idx2 in range(M // 2):  # 앞뒤 비교하는것
                    start = i + idx2
                    end = i + M - 1 - idx2
                    if arr[start][r] != arr[end][r]:
                        flag = False
                        break
                if flag:
                    for o in range(M):
                        ans += arr[i+o][r]
                    return len(ans)

for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    answer = palindrome(arr)
    print('#{} {}'.format(tc, answer))