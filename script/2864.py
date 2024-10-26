a, b = map(str, input().split())
max_sum = int(a.replace('5','6')) + int (b.replace('5','6'))
min_sum = int(a.replace('6','5')) + int (b.replace('6','5'))
print(min_sum, max_sum)