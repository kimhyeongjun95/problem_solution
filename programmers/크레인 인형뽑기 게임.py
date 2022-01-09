# 프로그래머스 카카오 크레인 인형뽑기 게임
def solution(board, moves):
    stack = []
    row = len(board)
    count = 0
    for move in moves:
        for i in range(row):
            if stack and stack[-1] == board[i][move-1]:
                stack.pop()
                board[i][move-1] = 0
                count += 2
                break
            if board[i][move-1]:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                break

    return count
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))