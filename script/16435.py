n, l = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for i in arr:
    if l >= i:
        l += 1
print(l)