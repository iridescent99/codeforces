

def number_of_ways(n, arr):
    if n < 3:
        return 0
    p = [0] * n
    p[0] = arr[0]
    count = 0
    for i in range(1, n):
        p[i] = p[i-1] + arr[i]
    total_sum = p[n-1]
    if total_sum % 3 != 0:
        return 0
    first_cuts = 0
    for i in range(n-1):
        if p[i] == 2 * (total_sum / 3):
            count += first_cuts
        if p[i] == total_sum / 3:
            first_cuts += 1
    return count



n = int(input())
arr = [int(num) for num in input().split()]
print(number_of_ways(n, arr))