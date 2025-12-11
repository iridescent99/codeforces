import math


def calc(n, m, a, b):
    min_spend = 0
    if b / m < a:
        remainder = n % m
        min_spend += math.floor(n / m) * b
        if remainder * a < b:
            min_spend += remainder * a
        else:
            min_spend += b
    else:
        min_spend = n * a
    print(min_spend)


if __name__ == "__main__":
    n, m, a, b = [int(l) for l in input().split()]
    calc(n, m, a, b)
