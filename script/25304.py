price = int(input())
for i in range(int(input())):
    product_price, cnt = map(int, input().split())
    price -= (product_price * cnt)
if price == 0:
    print('Yes')
else:
    print('No')