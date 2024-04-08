arr = [0 for _ in range(10)]
result = 1
for i in range(3):
    result *= int(input())

for i in list(str(result)):
    arr[int(i)] += 1

for i in arr:
    print(i)