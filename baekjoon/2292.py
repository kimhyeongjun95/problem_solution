# 백준 2292 벌집

n = int(input())
# 1       1개   1
# 2~7     6개   7
# 8~19    12개  19
# 20~37   18개  37
#               61
count = 1
i = 1
idx = 1
while n > i:
    i += (6*idx)
    idx += 1
    count += 1
print(count)