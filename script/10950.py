t = int(input())
arr = [list(map(int, input().split())) for _ in range(t)]
for s in arr:
    print(sum(s))