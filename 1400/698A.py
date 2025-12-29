import math


def vacations(arr, n):
    dp = [[0] * 3 for _ in range(n)]
    # 0 rest 1 contest 2 gym
    dp[0][1] = 1 if arr[0] in [1, 3] else 0
    dp[0][2] = 1 if arr[0] in [3, 2] else 0
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][1], max(dp[i - 1][2], dp[i - 1][0]))
        if arr[i] == 0:
            dp[i][1] = -math.inf
            dp[i][2] = -math.inf
        elif arr[i] == 1:
            dp[i][1] = 1 + max(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = -math.inf
        elif arr[i] == 2:
            dp[i][1] = -math.inf
            dp[i][2] = 1 + max(dp[i - 1][0], dp[i - 1][1])
        else:
            dp[i][1] = 1 + max(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] = 1 + max(dp[i - 1][0], dp[i - 1][1])
    max_active_days = max(dp[n - 1][0], max(dp[n - 1][1], dp[n - 1][2]))
    return n - max_active_days


n = int(input())
arr = [int(num) for num in input().split()]
print(vacations(arr, n))
