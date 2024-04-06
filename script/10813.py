n, m = map(int, input().split())
arr = [x for x in range(1,n+1)]
for index in range(m):
    i, j = map(int, input().split())
    i_x = arr[i-1]
    j_x = arr[j-1] 
    arr[i-1] = j_x
    arr[j-1] = i_x
for _ in arr:
    print(_, end=' ')