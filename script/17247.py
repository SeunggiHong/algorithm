n, m = map(int, input().split())

code = []

for i in range(n):
    a = str(input()).replace(' ','')
    if a.find('1') != -1:
        code.append([i, a.find('1')])
print(abs(code[1][0] - code[0][0])+ abs(code[1][1] - code[0][1]))