alphabet = list('abcdefghijklmnopqrstuvwxyz')
s = list(input())
arr = [-1]*26
for i in range(len(s)):
    for j in range(len(alphabet)):
        if s[i] == alphabet[j]:
            if arr[j] == -1:
                arr[j] = i
for _ in arr:
    print(_, end=' ')