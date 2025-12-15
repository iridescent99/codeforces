import math


def max_cost_permutation(n, p):
    start = math.inf
    end = -math.inf
    available_digits = [i for i in range(0, n+1) if i not in p]
    for i in range(n):
        if p[i] == 0 and available_digits[0] != i+1:
            start = min(start, i)
            end = max(end, i)
        elif p[i] != i+1 and p[i] != 0:
            start = min(start, i)
            end = max(end, i)
    if start < math.inf and end > -math.inf:
        return end-start+1
    return 0


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = [int(num) for num in input().split()]
        print(max_cost_permutation(n, p))
