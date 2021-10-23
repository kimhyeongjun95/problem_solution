# 백준 4673 셀프 넘버

result = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    
    result.add(i)

answer = [i for i in range(1, 10001) if i not in result]
for i in answer:
    print(i)