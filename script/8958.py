for i in range(int(input())):
    arr = list(input())
    score = 0
    sum_score = 0
    for j in arr:
        if j == 'O':
            score += 1
        else:
            score = 0
        sum_score += score
    print(sum_score)