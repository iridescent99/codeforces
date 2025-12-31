
def vanya_and_lanterns(n, l, arr):
    arr.sort()
    max_gap = 0
    for i in range(n+1):
        if 0 < i < n:
            max_gap = max(max_gap, arr[i]-arr[i-1])
        elif i == 0:
            max_gap = max(max_gap, arr[i] * 2)
        else:
            max_gap = max(max_gap, (l-arr[i-1]) * 2)
    return max_gap / 2


n, l = [int(num) for num in input().split()]
arr = [int(num) for num in input().split()]
print(vanya_and_lanterns(n, l, arr))
