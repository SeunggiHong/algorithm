k = int(input())
arr = []
for i in range(k):
    zero = int(input())
    if zero == 0:
        arr.pop(-1)
    else:
        arr.append(zero)
print(sum(arr))