# t = int(input())

# for test_case in range(1, t+1):
#     n, m = map(int, input().split())
#     a = list(map(int, input().split())
#     b = list(map(int, input().split()))

#     max_list, min_list = max(a, b), min(a, b)
#     for i in range(max_list):
#         for j in range(min_list):

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    count = 1

    check = [0 for _ in range(10)] # [0, 0, 0, .....]

    #1. 들어오는 숫자를 증가시키는 로직
    #2. 배수가 된 숫자에서 0~9 뽑아내는 로직
    #3. 뽑아낸 숫자를 어딘가에 "표시"하는 로직
    #4. check 리스트가 전부 다 표기되었는지 확인하는 로직
    # => 그런데 언제? 정확히 어느 위치에서?

    result = None
    while True:
        number = str(n * count) # 1N => 2N => 1, 2, 3, 4
        for num in number:
            idx = int(num) # num을 인덱스로 활용해서 체크
            check[idx] = 1

        is_all_checked = True
        for i in check: # 0, 1, 1, (인덱스가 아니라 실제 값)
            if i == 0:
                is_all_checked = False
                break
        
        if is_all_checked:
            result = number
            break # 모든 리스트의 요소가 1로 채워져 있음 => while문 종료
            
        count += 1

    return result
