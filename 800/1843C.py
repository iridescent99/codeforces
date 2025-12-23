import math


def sum_in_binary_tree(n):
    total = 0
    while n >= 1:
        total += n
        n //= 2
    return total


t = int(input())
for _ in range(t):
    n = int(input())
    print(sum_in_binary_tree(n))