# 프로그래머스 이중우선순위 큐
# import heapq
# def solution(operations):
#     answer = []
#     heap = []
#     for operation in operations:
#         c, n = operation.split(' ')
#         if c == 'I':
#             heapq.heappush(heap, int(n))
#         else:
#             if heap:
#                 if n == '1': # 최대값
#                     heap.pop(heap.index(heapq.nlargest(1, heap)))
#                 else: # 최소값
#                     heapq.heappop(heap)

def solution(operations):
    answer = []
    for operation in operations:
        c, n = operation.split(' ')
        if c == 'I':
            answer.append(int(n))
        else:
            if answer:
                if n == '1':
                    answer.pop()
                else:
                    answer.pop(0)
        answer.sort()
    if not answer:
        return [0,0]
    else:
        return [max(answer), min(answer)]

print(solution(["I 16","D 1"])) # [0, 0]
print(solution(["I 7","I 5","I -5","D -1"])) # [7, 5]

