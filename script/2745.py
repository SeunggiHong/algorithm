alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = input().split()
n = ''.join(reversed(n))
b = int(b)
result = 0
for i in range(len(n)-1,-1,-1):
    result += alphabet.index(n[i]) * (b**i)
print(result)