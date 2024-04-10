import math

for i in range(int(input())):
    x, y = map(int, input().split())
    print(math.factorial(y)//(math.factorial(x)*math.factorial(y-x)))