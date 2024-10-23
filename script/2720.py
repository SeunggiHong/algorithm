t = int(input())
answer = []
for i in range(t):
    q,d,n,p = 0,0,0,0
    pay = int(input())

    if pay//25 > 0:
        q = pay//25
        pay = pay%25
    if pay//10 > 0:
        d = pay//10
        pay = pay%10
    if pay//5 > 0:
        n = pay//5
        pay = pay%5
    if pay//1 > 0:
        p = pay//1
        pay = pay%1
    answer.append([q,d,n,p])

for i in answer:
    for j in i:
        print(j, end=' ')
    print()