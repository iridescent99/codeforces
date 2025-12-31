import math


def given_length_and_sum_of_digits(m, s):
    max_num = min_num = 0
    s_max = s_min = s
    for i in range(m):
        max_digit = min(s_max, 9)
        max_num += max_digit * 10**(m-1-i)
        s_max -= max_digit

        for j in range(10):
            if j == 0 and i == 0 and m > 1:
                continue
            if s_min - j <= 9 * (m-i-1):
                s_min -= j
                min_num += j * 10**(m-1-i)
                break

    if s_max == s_min == 0:
        return min_num, max_num
    return -1, -1


m, s = [int(num) for num in input().split()]
print(*given_length_and_sum_of_digits(m, s))