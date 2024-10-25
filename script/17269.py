alpha = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 2,
    'E': 4,
    'F': 3,
    'G': 1,
    'H': 3,
    'I': 1,
    'J': 1,
    'K': 3,
    'L': 1,
    'M': 3,
    'N': 2,
    'O': 1,
    'P': 2,
    'Q': 2,
    'R': 2,
    'S': 1,
    'T': 2,
    'U': 1,
    'V': 1,
    'W': 1,
    'X': 2,
    'Y': 2,
    'Z': 1
}

n, m = map(int, input().split())
name_1, name_2 = map(str, input().split())

sum_name = ''

for i in range(min(n,m)):
    sum_name += name_1[i] + name_2[i]

if n < m :
    sum_name += name_2[n:]
elif n > m:
    sum_name += name_1[m:]

arr = []
for i in sum_name:
    arr.append(alpha[i])

while True:
    arr_2 = []
    if len(arr) == 2:
        print(str(int(str(arr[0])+str(arr[1])))+'%')
        break
    for i in range(1,len(arr)):
        if arr[i-1] + arr[i] < 10:
            arr_2.append(arr[i-1] + arr[i])
        else:
            arr_2.append((arr[i-1] + arr[i])%10)
    arr = arr_2