sosu = [2]
for i in range(3,1001):
    arr = []
    for j in range(1,i):
        if i%j == 0:
            arr.append(j)
    if len(arr) == 1:
        sosu.append(i)
cnt = 0
n = int(input())
in_arr = list(map(int, input().split()))
for i in in_arr:
    if i in sosu:
        cnt += 1

print(cnt)