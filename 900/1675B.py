import math


def make_it_increasing(n, arr):
    count = 0
    for i in range(n - 2, -1, -1):
        while i < n - 1 and arr[i] >= arr[i + 1]:
            if arr[i] == 0:
                return -1
            arr[i] = math.floor(arr[i] / 2)
            count += 1
        i -= 1
    return count


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(num) for num in input().split()]
    print(make_it_increasing(n, arr))
