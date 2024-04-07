n, m = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(m)]

for i in range(2):
    for j in range(n):
        arr = list(map(int, input().split()))
        for z in range(len(arr)):
            matrix[j][z] += arr[z]

for i in matrix:
    for j in i:
        print(j, end=' ')
    print()