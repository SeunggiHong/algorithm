current_h, current_m = map(int, input().split())
have_m = int(input()) 

current_h += have_m // 60
current_m += have_m % 60

if current_m >= 60:
    current_h += 1
    current_m -= 60
if current_h >= 24:
    current_h -= 24

print(current_h,current_m)
