import math


def make_array_good(n, arr):
    gcd = math.gcd(*arr)
    max_val = max(arr)
    k = max_val // gcd
    target = k * gcd
    manipulations = []
    for i in range(n):
        if arr[i] == max_val:
            gap = target - max_val
            j = arr[i]
            while gap > 0 and j > 0:
                if j <= gap:
                    manipulations.append((i, j))
                    gap -= j
                    j = arr[i] + j
                else:
                    j -= 1
            arr[i] = target
        else:
            if target % arr[i] != 0:
                j = arr[i]
                while target % arr[i] != 0 and j > 0:
                    if j <= target-arr[i]:
                        manipulations.append((i, j))
                        arr[i] += j
                        j = arr[i]
                    else:
                        j -= 1
    print(len(manipulations))
    for k, v in manipulations:
        print(f"{k} {v}")


t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(num) for num in input().split()]
    make_array_good(n, a)
