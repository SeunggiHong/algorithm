n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))
result = {}

for i in range(n):
    result[n_arr[i]] = 0

for i in range(m):
    if m_arr[i] not in result:
        print(0, end=' ')
    else:
        print(1, end=' ')