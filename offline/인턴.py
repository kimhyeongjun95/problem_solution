from collections import deque
def solution(sentence, keyword, skips):
    answer = ''
    keyword = deque(list(keyword))
    sentence = deque(list(sentence))

    flag = False
    for i in range(len(skips)):
        while skips[i]: # 스킵이 있고
            if not sentence:
                flag = True
                break
            popped = sentence.popleft()
            answer += popped
            if popped == keyword[0]:
                break
            skips[i] -= 1
        if flag:
            break
        popped_k = keyword.popleft()
        answer += popped_k
        keyword.append(popped_k)

    
    while sentence:
        popped = sentence.popleft()
        answer += popped

    # if sum(skips):
    #     for i in range(len(skips)):
    #         while skips[i]:
    #             popped_k = keyword.popleft()
    #             answer += popped_k
    #             keyword.append(popped_k)
    #             skips[i] -= 1
    #             print(skips, answer)

    return answer




print(solution("i love coding", "mask", [0, 0, 3, 2, 3, 4])) # 21
print(solution("i love coding", "mode", [0, 10])) # "mi loove coding"
print(solution("abcde fghi", "axyz", [3, 9, 0, 1])) # "aabcde fghixy"

