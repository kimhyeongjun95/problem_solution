t = int(input())

cp_a = 0
cp_b = 0

for i in range(1, t+1):
    p, q, r, s, w = map(int, input().split())
    
    cp_a = p * w
    
    if w < r:
        cp_b = q
    elif w > r:
        cp_b = q + ((w-r) * s)

    if cp_a < cp_b:
        print(f'#{i} {cp_a}')
    else:
        print(f'#{i} {cp_b}')