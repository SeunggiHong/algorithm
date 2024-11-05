n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

temp = []

def dfs():
    if len(temp) == m:
        print(*temp)
        return
    for i in range(n):
        if arr[i] not in temp:
            temp.append(arr[i])
            dfs()
            temp.pop()

dfs()