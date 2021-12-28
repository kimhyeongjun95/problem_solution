# 프로그래머스 최대공약수와 최소공배수

# 최대공약수, 최소공배수 순
def solution(n, m):
    if n > m:
        n, m = m, n
    
    a, b = n, m
    while b:
        a, b = b, a%b
    return [a, n*m//a]

print(solution(3, 12)) # [3, 12]
print(solution(2, 5)) # [1, 10]