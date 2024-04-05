dice = list(map(int, input().split()))
cnt = [0 for _ in range(len(dice))]
for i in range(len(dice)):
    current = dice[i]
    for j in range(len(dice)):
        if current == dice[j]:
            cnt[i] += 1
if max(cnt) == 3:
    print(10000+dice[0]*1000)
elif max(cnt) == 2:
    print(1000+dice[cnt.index(max(cnt))]*100)
else :
    print(max(dice) * 100)