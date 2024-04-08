n = int(input())
honeycomb = 1
for i in range(n):
    honeycomb += i*6
    if n <= honeycomb:
        print(i+1)
        break