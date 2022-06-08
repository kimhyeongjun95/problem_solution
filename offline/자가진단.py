def solution(arr):
    arr.sort()
    answer = []
    stack = []
    last = 0
    count = 1
    for i in arr:
        if not stack:
            stack.append(i)
            continue

        if stack and stack[-1] == i:
            count += 1
        if stack and stack[-1] != i:
            stack.pop()
            stack.append(i)
            if count >= 2:
                answer.append(count)
            count = 1
    if count >= 2:
        answer.append(count)
    
    if answer:
        return answer
    return [-1]
        

print(solution([1, 2, 3, 3, 3, 3, 4, 4]))
# [4, 2]
print(solution([3, 2, 4, 4, 2, 5, 2, 5, 5]))
# [3, 2, 3]
print(solution([3, 5, 7, 9, 1]))
# [-1]