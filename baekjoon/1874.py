# 1874 스택 수열
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음 // 하나의 수열

# 스택에 push하는 순서는 반드시 오름차순을 지킨다.

# 1부터 n까지에 수에 대해 차례로 
# [push, push, push, push, pop, pop, push, push, pop, push, push, pop, pop, pop, pop, pop]
# 연산을 수행하면 수열 [4, 3, 6, 8, 7, 5, 2, 1]을 얻을 수 있다.

# -> 4가 append 되었을때 pop하면 되는거 같다.
# -> 즉 출력은 그 과정을 보여줘야 한다.

# 1. n의 갯수만큼 입력을 미리 받아놓는다.
# 2. n의 갯수만큼의 반복문
# 3. 4가 들어올때까지 + 출력 / 그 다음에 pop과 - 출력

n = int(input())
count = 1
arr = []
answer = []
flag = False
for _ in range(n):
    number = int(input())
    
    while count <= number:
        arr.append(count)
        answer.append('+')
        count += 1

    if arr[-1] == number:
        arr.pop()
        answer.append('-')
    elif arr[-1] > number:
        flag = True

if flag:
    print('NO') 
else:
    for i in answer:
        print(i)
