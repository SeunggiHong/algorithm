from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    else:
        lst = list(combinations(arr[1:], 6))
        for i in lst:
            for j in i:
                print(j,end=' ')
            print()
        print()