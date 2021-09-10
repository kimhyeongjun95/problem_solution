# a : 금kg
# b : 은kg
# i번 도시 : 금: g[i] / 은: s[i] 보유
# 편도로 t[i]시간 / 최대 w[i] kg 광물 운반

# 가장 빠른 시간 return하기

# 20시간 왕복..
# 7,0 / 3, 4 / 0,6

# 모든 도시에서 왕국으로 갖다주는 거임.

# 1. 각 도시마다 g s w t 받아보기
# 2. 보유량 다 갖다줄때까지 얼마나 걸리는지 계산하기
# 3. answer = 0에서 a,b 까지 언제 도달하는지 계산

def solution(a, b, g, s, w, t):
    temp = []
    for i in range(len(g)):
        temp.append((g[i], s[i], w[i], t[i]))
    
    temp = sorted(temp, key=lambda x : x[3]) # 시간순으로 정렬
    
    time = 0
    answer = []
    while time < 200:
        for i in range(len(g)):
            if a and g[i] and w[i] >= a:
                g[i] -= a
                a = 0
                answer.append(time+t[i])
            elif a and g[i]: # 금을 더 가져가야하고 i도시에 금을 더 가져가야 한다면..
                if time % (2 * t[i]) == 0:
                    g[i] -= w[i]
                    a -= w[i]
                    
            if b and s[i] and w[i] >= b:
                s[i] -= b
                b = 0
                answer.append(time+t[i])
            elif b and s[i]: # 은을 더 가져가야하고 i 도시에 은을 더 가져가야 한다면..
                if time % (2 * t[i]) == 0:
                    s[i] -= w[i]
                    b -= w[i]
        time += 1
        print(a, b, g, s, w, t, time)
        
    return answer

a = 10
b = 10
g = [100]
s = [100]
w = [7]
t = [10]
print(solution(a, b, g, s, w, t))