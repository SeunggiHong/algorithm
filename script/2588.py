first_num = int(input())
sec_num = list(input())
result = []
for i in sec_num[::-1]:
    result.append(first_num * int(i))
    print(first_num * int(i))

for i in range(len(result)):
    result[i] *= 10**i

print(sum(result))