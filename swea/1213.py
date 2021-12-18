# SWEA 1213 String

for _ in range(1, 11):
    tc = int(input())
    s = input()
    word = input()

    count = 0
    for i in range(len(word)-len(s)+1):
        if word[i:i+len(s)] == s:
            count += 1
            
    print(f'#{tc} {count}')
