n, k = map(int, input().split())
arr = []
for i in range(n,0,-1):
    if n % i == 0:
        arr.append(n//i)

if len(arr) == 0 or len(arr) < k:
    print(0)
else:
    print(arr[k-1])