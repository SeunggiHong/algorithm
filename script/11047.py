coin = []
n, k = map(int,input().split())
cnt = 0
for i in range(n):
    coin.append(int(input()))

while k != 0:
    for i in range(n-1,-1,-1):
        if coin[i] <= k:
            cnt += k//coin[i]
            k = k%coin[i]
print(cnt)