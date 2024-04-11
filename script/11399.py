n = int(input())
per_time = list(map(int, input().split()))

per_time.sort(reverse=True)
time = 0
for i in range(n):
    cnt = 0
    for j in range(i,n):
        cnt += per_time[j]
    time += cnt
    
print(time)
