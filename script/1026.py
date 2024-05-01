n = int(input())
a_arr = sorted(list(map(int, input().split())))
b_arr = sorted(list(map(int, input().split())), reverse=True)
result = 0
for i in range(n):
    result += b_arr[i] * a_arr[i]
print(result)