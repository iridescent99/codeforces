import math

def kth_not_divisible(n, k):
    return(k-1)//(n-1) + k


t = int(input())
for _ in range(t):
    n, k = [int(num) for num in input().split()]
    print(kth_not_divisible(n, k))