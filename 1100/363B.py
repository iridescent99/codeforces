import math

def fence(n, k, heights):
    P = [0] * n
    P[0] = heights[0]
    for i in range(1, n):
        P[i] = P[i-1] + heights[i]
    min_sum = math.inf
    ind = -1
    for i in range(n):
        j = k + i - 1
        if j < n:
            total_height = P[j]
            if i > 0:
                total_height -= P[i-1]
            if total_height < min_sum:
                min_sum = total_height
                ind = i
    return ind + 1



n, k = [int(num) for num in input().split()]
heights = [int(nm) for nm in input().split()]
print(fence(n,k, heights))