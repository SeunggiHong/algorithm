n = int(input())
m = set()
for i in range(n):
    m.add(int(input()))

m = list(m)
m.sort()
for i in m:
    print(i)