exp = list(input().split('-'))
arr = []
for i in exp:
    plus = i.split('+')
    num = 0
    for j in plus:
        num += int(j)
    arr.append(num)

answer = arr[0]
for i in range(1,len(arr)):
    answer -= arr[i]

print(answer)