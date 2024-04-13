import sys

n = int(sys.stdin.readline())
result = []
for i in range(n):
    arr = list(sys.stdin.readline().strip())
    if list(reversed(arr)) == arr:
        result.append(0)
    else:
        flag = False
        for i in range(len(arr)):
            ex_arr = arr.copy()
            ex_arr.pop(i)
            if list(reversed(ex_arr)) == ex_arr:
                flag = True
        if flag:
            result.append(1)
        else:
            result.append(2)

for _ in result:
    print(_)