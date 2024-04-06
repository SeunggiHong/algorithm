n = int(input())
arr = list(map(int, input().split()))
max_score = max(arr)
for i in range(n):
    arr[i] = arr[i]/max_score*100
print(sum(arr)/len(arr))