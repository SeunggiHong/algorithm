arr = set(range(1,10001))
arr_b = set()

for i in arr:
    num = i
    for j in str(i):
        num += int(j)
    arr_b.add(num)

for i in sorted(arr-arr_b):
    print(i)