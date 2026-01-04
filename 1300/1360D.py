import math


def buying_shovels(n, k):
    max_package = 1
    for i in range(1, math.ceil(math.sqrt(n))+1):
        if n % i == 0:
            if i <= k:
                max_package = max(max_package, i)
            if n//i <= k:
                max_package = max(max_package, n//i)
    return n//max_package


t = int(input())
for _ in range(t):
    n, k = [int(num) for num in input().split()]
    print(buying_shovels(n, k))
