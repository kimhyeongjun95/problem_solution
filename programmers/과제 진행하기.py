# 프로그래머스 과제 진행하기

def solution(plans):
    arr = []
    for plan in plans:
        name, start, playtime = plan
        hour, min = map(int, start.split(':'))
        time = (hour * 60) + min
        arr.append((name, time, int(playtime)))
    arr.sort(key = lambda x: x[1])

    stack = []
    now = 0
    answer = []
    for i in range(len(arr)):
        now = arr[i][1]
        name, time, playtime = arr[i]   
        if i < len(arr)-1 and time + playtime > arr[i+1][1]:
            stack.append((name, playtime - (arr[i+1][1] - time)))
        else:
            answer.append(name)
            now += playtime
            while i < len(arr)-1 and stack and stack[-1][1] + now <= arr[i+1][1]:
                lastName, lastTime = stack.pop()
                answer.append(lastName)
                now += lastTime
            if i < len(arr)-1 and stack and stack[-1][1] + now > arr[i+1][1]:
                lastName, lastTime = stack.pop()
                lastTime -= arr[i+1][1] - now
                stack.append((lastName, lastTime))
            while i == len(arr)-1 and stack:
                popped = stack.pop()
                answer.append(popped[0])

    return answer

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
# ["korean", "english", "math"]
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# ["science", "history", "computer", "music"]