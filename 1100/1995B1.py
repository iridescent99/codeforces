

def bouquet_easy(n, m, flowers):
    left, right = 0, 1
    flowers.sort()
    sum_window = flowers[0]
    running_max = sum_window if sum_window <= m else 0
    while left <= right < n:
        if flowers[right] - flowers[left] > 1 or sum_window + flowers[right] > m:
            sum_window -= flowers[left]
            left += 1
        else:
            sum_window += flowers[right]
            running_max = max(running_max, sum_window)
            right += 1

    return running_max



t = int(input())
for _ in range(t):
    n, m = [int(num) for num in input().split()]
    flowers = [int(num) for num in input().split()]
    print(bouquet_easy(n, m, flowers))