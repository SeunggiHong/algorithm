a, b = map(int ,input().split())
arr = [a+b, a-b, a*b, int(a/b), a%b]
for _ in arr:
    print(_)