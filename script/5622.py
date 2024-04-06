arr = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
text = list(input())
time = 0
for t in text:
    for i in range(len(arr)):
        if t in arr[i]:
            time += (i+3)
print(time)