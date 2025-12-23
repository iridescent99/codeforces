import math

def negatives_and_positives(n, arr):
    abs_min = math.inf
    parity = True
    for i in range(n):
        abs_min = min(abs_min, abs(arr[i]))
        if arr[i] < 0:
            parity = not parity
    total_sum =  sum(abs(num) for num in arr)
    if parity:
        return total_sum
    return total_sum - 2 * abs_min

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(num) for num in input().split()]
    print(negatives_and_positives(n, arr))
