from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int,input().split()))

max_num = 0

for i in list(combinations(arr,3)):
    if sum(i) > max_num and sum(i) <= m:
        max_num = sum(i)
print(max_num)