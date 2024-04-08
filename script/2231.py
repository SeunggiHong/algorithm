n = int(input())
creater = []
for i in range(1,n+1):
    text = str(i)
    t_case = i
    for j in text:
        t_case += int(j)
    if n == t_case:
        creater.append(i)

if len(creater) == 0:
    print(0)
else:
    print(creater[0])