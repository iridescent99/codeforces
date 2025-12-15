import math


def cunning_seller(n):
    if n < 3:
        return n * 3
    dealA = n % 3
    dealB = int((n-dealA) / 3)
    return dealA * 3 + dealB * 10



if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(cunning_seller(n))