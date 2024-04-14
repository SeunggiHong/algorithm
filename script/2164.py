from collections import deque

n = deque([x for x in range(1,int(input())+1)])

while True:
    if len(n) == 1:
        print(n[0])
        break
    else:
        n.popleft()
        a = n.popleft()
        n.append(a)