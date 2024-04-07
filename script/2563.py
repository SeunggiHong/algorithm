t = int(input())
matrix = [[0 for _ in range(100)] for _ in range(100)]

for i in range(t):
    x, y = map(int, input().split())
    for ix in range(x,x+10):
        for iy in range(y,y+10):
            matrix[ix][iy] += 1
cnt = 0
for i in matrix:
    for j in i:
        if j > 0:
            cnt += 1

print(cnt)