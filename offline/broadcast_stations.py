
def rest_finder(arr):
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                count += 1
    return count

def station_finder(arr):
    location = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                location.append((i, j))
    return location

def house_keeper(arr, location):
    for k, l in location:
        print(arr[k][l])
        if arr[k+1][l] == 'H':
            arr[k+1][l] = 'X'
        if arr[k-1][l] == 'H':
            arr[k-1][l] = 'X'
        if arr[k][l+1] == 'H':
            arr[k][l+1] = 'X'
        if arr[k][l-1] == 'H':
            arr[k][l-1] = 'X'
    
    return arr

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(str, input())) for _ in range(n)]

    location = station_finder(arr)
    arr = house_keeper(arr, location)
    answer = rest_finder(arr)
    print(location)
    # for i in arr:
        # print(i)
    print(answer)
    