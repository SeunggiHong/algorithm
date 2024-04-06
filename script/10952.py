arr = []
while True:
    a, b = map(int, input().split())
    if a+b == 0:
        for i in arr:
            print(sum(i))
        break
    else:
        arr.append([a,b])