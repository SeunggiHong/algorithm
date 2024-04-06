t = int(input())
result = []
for i in range(t):
    text = input()
    result.append(text[0]+text[-1])
for _ in result:
    print(_)