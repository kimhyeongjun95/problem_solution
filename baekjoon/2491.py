import sys

n = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))
continuous = []
result_list = []
count = 2
continuous.append(numbers[0])
continuous.append(numbers[1])
# print(continuous)
# print(numbers)
if len(numbers) > 2:
    for i in range(2, len(numbers)-1):
        if continuous[-1] >= continuous[-2]:
            if numbers[i] < continuous[-1]:
                result_list.append(count)
                count = 2

            elif numbers[i] >= continuous[-1]:
                count += 1
                
        elif continuous[-2] >= continuous[-1]:
            if continuous[-1] >= numbers[i]:
                count += 1
            
            elif numbers[i] > continuous[-1]:
                result_list.append(count)
                count = 2
        continuous.append(numbers[i])
    if numbers[-1] >= continuous[-2] and continuous[-2] >= continuous[-3]:
        count += 1
        result_list.append(count)
    elif numbers[-1] <= continuous[-2] and continuous[-2] <= continuous[-3]:
        count +=1
        result_list.append(count)
    elif numbers[-1] > continuous[-2] and continuous[-2] < continuous[-3]:
        result_list.append(count)
    elif numbers[-1] < continuous[-2] and continuous[-2] > continuous[-3]:
        result_list.append(count)
    print(max(result_list))
    
else:
    print(2)