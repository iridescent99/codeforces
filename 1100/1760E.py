

def binary_inversions(n, arr):
    zero_count = [0] * (n+1)
    zero_count[-1] = 0
    one_count = [0] * (n+1)
    one_count[0] = 0
    inversions = 0
    for i in range(n-1, -1, -1):
        zero_count[i] = zero_count[i+1] + int(not arr[i])
    for i in range(n):
        one_count[i] = one_count[i-1] + arr[i]
        if arr[i] == 1:
            inversions += zero_count[i+1]
    max_diff = 0
    for i in range(0, n):
        if arr[i] == 0:
            diff = zero_count[i+1] - one_count[i-1]
        else:
            diff = one_count[i-1] - zero_count[i+1]
        if diff > max_diff:
            max_diff = diff
    return inversions + max_diff




t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(num) for num in input().split()]
    print(binary_inversions(n, arr))