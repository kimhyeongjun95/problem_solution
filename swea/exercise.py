# SWEA 1983 조교의 성적 매기기

# 총점 = 중간 35% 기말 45% 과제 20%

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split()) # n은 10의 배수
    students = []
    for i in range(n):
        middle, final, task = map(int, input().split())
        score = (middle*0.35) + (final*0.45) + (task*0.2)
        students.append(score)
    
    students.sort(reverse=True)
    count = n // 10
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    idx = int(students.index(students[k-1]) / count)
    answer = grades[idx]
    print(f'#{tc} {answer}')