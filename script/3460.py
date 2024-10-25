t = int(input())
result = [[] for _ in range(t)]
for i in range(t):
    binary = list(reversed(str(bin(int(input())))[2:]))
    for j in range(len(binary)):
        if binary[j] == '1':
            result[i].append(j)

for i in result:
    for j in i:
        print(j, end=' ')
    print()
