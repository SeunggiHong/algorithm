n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

def dfs(v, visited=[]):
    visited.append(v)
    for i in graph[v]:
        if not i in visited:
            visited = dfs(i, visited)
    return visited

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(len(dfs(1))-1)