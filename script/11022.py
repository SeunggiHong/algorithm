t = int(input())
arr = [list(map(int, input().split())) for _ in range(t)]
for i in range(1, len(arr)+1):
    print("Case #{}: {} + {} = {}".format(i, arr[i-1][0], arr[i-1][1], sum(arr[i-1])))