import math


def find_greatest(arr):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    for p in primes:
        for num in arr:
            if num % p != 0:
                return p
    return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        _ = int(input())
        arr = [int(i) for i in input().split()]
        print(str(find_greatest(arr)))
