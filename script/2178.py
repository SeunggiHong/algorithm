from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(n)]

def bfs(x, y, graph):
    que = deque()
    que.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
                
    return graph[n-1][m-1]

cnt = bfs(0,0,matrix)
print(cnt)