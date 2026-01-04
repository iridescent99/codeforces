import math


def calculate_primes():
    is_prime = [True] * 1000001
    is_prime[0] = is_prime[1] = False
    for i in range(2, 1001):
        if is_prime[i]:
            count = len(is_prime[i*i::i])
            is_prime[i*i::i] = [False] * count
    return is_prime




def t_primes(n, arr):
    is_prime = calculate_primes()
    for num in arr:
        t_prime = False
        is_perfect_square = math.sqrt(num).is_integer()
        if is_perfect_square:
            if is_prime[int(math.sqrt(num))]:
                print("YES")
                continue
        print("NO")


n = int(input())
arr = [int(num) for num in input().split()]
t_primes(n, arr)