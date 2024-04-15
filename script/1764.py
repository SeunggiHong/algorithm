n, m = map(int, input().split())
n_arr = set()
m_arr = set()

for i in range(n):
    n_arr.add(input())
for i in range(m):
    m_arr.add(input())

result = sorted(list(n_arr & m_arr))

print(len(result))
for _ in result:
    print(_)