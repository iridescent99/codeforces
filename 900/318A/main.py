import math


def even_odds(n, k):
    boundary = math.ceil(n / 2)
    if k <= boundary:
        target = k - 1
        start = 1
    else:
        target = k - math.ceil(n / 2) - 1
        start = 2
    return start + 2 * target


if __name__ == "__main__":
    n, k = [int(n) for n in input().split()]
    print(even_odds(n, k))
