def bfs(graph,start):
    from collections import deque

    queue = deque([start])
    visited = set([start])

    while queue:
        current = queue.popleft()
        for next_node in graph[current]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    return visited

t = int(input())

answer = []

for i in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for j in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    visited = bfs(graph, 1)
    answer.append(len(visited) -1)

for _ in answer:
    print(_)