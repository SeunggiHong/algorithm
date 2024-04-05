a, b, c = map(int,input().split())
arr = [
    (a+b)%c,
    ((a%c)+(b%c))%c,
    (a*b)%c,
    ((a%c)*(b%c))%c
]
for _ in arr:
    print(_)