
def solution(N, stages):
    # 실패율 : 도달했으나 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수 
    # N : 스테이지 개수
    # stages : 사용자가 현재 멈춰있는 스테이지의 번호 배열

    # 실패율 구하기
    # answer 리스트에 현재 스테이지와 실패율 저장

    idx = 1
    length = len(stages)
    result = []
    while idx <= N:
        cnt = stages.count(idx)
        
        if length == 0:
            fail = 0
        else:
            fail = cnt / length
        
        result.append((idx, fail))
        length -= cnt

        idx += 1
    
    result = sorted(result, key=lambda x: x[1], reverse=True)
    answer = []
    for i in result:
        answer.append(i[0])
    
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) #	[3,4,2,1,5]
print(solution(4, [4,4,4,4,4]))	#               [4,1,2,3]