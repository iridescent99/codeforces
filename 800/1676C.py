import math


def most_similar_words(n, m, s):
    min_difference = math.inf
    for ref_i in range(n):
        for compare_i in range(n):
            min_difference_ref = 0
            if ref_i == compare_i:
                continue
            for letter_i in range(m):
                min_difference_ref += abs((ord(s[ref_i][letter_i]) - 96) - (ord(s[compare_i][letter_i]) - 96))
            min_difference = min(min_difference_ref, min_difference)
    return min_difference



t = int(input())
for _ in range(t):
    n, m = [int(num) for num in input().split()]
    s = []
    for _ in range(n):
        s.append(input())
    print(most_similar_words(n, m, s))
