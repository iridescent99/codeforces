import math


def twins(n, arr):
    arr.sort()
    coin_count = 0
    total_sum = sum(arr)
    twin_sum = 0
    threshold = math.ceil(total_sum / 2) if total_sum % 2 != 0 else (total_sum // 2) + 1
    j = n - 1
    while j >= 0 and twin_sum < threshold:
        twin_sum += arr[j]
        arr[j] = -99
        coin_count += 1
        j -= 1
    if twin_sum >= threshold:
        return coin_count
    for i in range(n):
        if arr[i] + twin_sum >= threshold:
            return coin_count + 1
    return coin_count


n = int(input())
arr = [int(num) for num in input().split()]
print(twins(n, arr))
