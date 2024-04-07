matrix = []
for i in range(9):
    matrix.append(list(map(int, input().split())))

max_num = 0
max_locate = [0,0]
for i in range(9):
    for j in range(9):
        if matrix[i][j] >= max_num:
            max_num = matrix[i][j]
            max_locate = [i+1,j+1]

print(max_num)
for _ in max_locate:
    print(_, end=' ')