mbti = input()
n = int(input())
cnt = 0
for i in range(n):
    if input() == mbti:
        cnt += 1
print(cnt)