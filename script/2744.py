text = input()
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
down = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(text)):
    for j in range(len(up)):
        if text[i] == up[j]:
            print(down[j], end='')
        if text[i] == down[j]:
            print(up[j], end='')