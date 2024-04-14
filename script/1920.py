n = int(input())
a_arr = set(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

for i in m_arr:
    print(1) if i in a_arr else print(0)