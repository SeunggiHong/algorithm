cost = 1000 - int(input())

coin_cnt = 0

if cost//500 > 0:
    coin_cnt += cost//500
    cost = cost%500
if cost//100 > 0:
    coin_cnt += cost//100
    cost = cost%100
if cost//50 > 0:
    coin_cnt += cost//50
    cost = cost%50
if cost//10 > 0:
    coin_cnt += cost//10
    cost = cost%10
if cost//5 > 0:
    coin_cnt += cost//5
    cost = cost%5
if cost//1 > 0:
    coin_cnt += cost//1
    cost = cost%1

print(coin_cnt)