# 1은 on 0은 off

n = int(input())
switches = list(map(int, input().split()))
s_number = int(input())

# 남자는 자신의 배수
# 여자는 자신을 중심으로

for _ in range(s_number):
    gen, num = map(int, input().split())

    if gen == 1: # 남자라면
        for i in range(len(switches)):
            if (i+1) % num == 0:
                if switches[i] == 0:
                    switches[i] = 1
                else:
                    switches[i] = 0
        # print(switches)
    
    else: # 여자라면
        idx = 1
        num -= 1 # 인덱싱 편의
        if switches[num] == 1:
            switches[num] = 0
        else:
            switches[num] = 1
        

        while num - idx >= 0 and num + idx < len(switches):
            if switches[num+idx] == switches[num-idx]:
                if switches[num+idx] == 1:
                    switches[num+idx] = 0
                    switches[num-idx] = 0
                else:
                    switches[num+idx] = 1
                    switches[num-idx] = 1
            else:
                break

            idx += 1
        num += 1

for i in range(len(switches)):
    if i and i % 20 == 0:
        print()
    print(switches[i], end=' ')