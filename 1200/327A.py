

def flipping_game(arr, n):
    cum_sum = [0] * (n+1)
    cum_sum[0] = arr[0]
    total_ones = sum(arr)
    for i in range(1, n+1):
        cum_sum[i] = cum_sum[i-1] + arr[i-1]
    max_sum = 0
    for i in range(n):
        for j in range(i, n):
            ones_in_range = cum_sum[j + 1] - cum_sum[i]
            length = j - i + 1
            zeros_in_range = length - ones_in_range

            current_ones = total_ones - ones_in_range + zeros_in_range

            max_sum = max(max_sum, current_ones)
    return max_sum




n = int(input())
arr = [int(num) for num in input().split()]
print(flipping_game(arr, n))