from itertools import combinations

n, m = map(int, input().split())
if m == 1:
    for i in range(n):
        print(i+1)
else:
    arr = list(combinations([x for x in range(1,n+1)], m))
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()