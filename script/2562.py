max_num = 0
cnt = 0
for i in range(9):
    num = int(input())
    if max_num < num:
        max_num = num
        cnt = i


print(max_num)
print(cnt+1)
