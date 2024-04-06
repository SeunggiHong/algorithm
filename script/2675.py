t = int(input())
result = []
for i in range(t):
    r, s = map(str ,input().split())
    rs = ''
    for j in s:
        rs += j*int(r)
    result.append(rs)

for _ in result:
    print(_)