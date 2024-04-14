from itertools import combinations
L, C = map(int, input().split())
alphabets = input().split()
alpha_combs = combinations(sorted(alphabets), L)

answer = []

for alpha_comb in alpha_combs:
    consonant_count = 0
    vowel_count = 0

    for alpha in alpha_comb:
        if alpha in "aeiou":
            consonant_count += 1
        else:
            vowel_count += 1

    if consonant_count >= 1 and vowel_count >= 2:
        print("".join(alpha_comb))