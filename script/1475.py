n = list(input())
arr = [0 for _ in range(10)]
for i in n:
    if int(i) == 6 or int(i) == 9:
        if arr[6] <= arr[9]:
            arr[6] += 1
        else:
            arr[9] += 1
    else:
        arr[int(i)] += 1
print(max(arr))