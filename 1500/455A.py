def boredom(arr):
    limit = max(arr)
    count = [0] * (limit + 1)
    for x in arr:
        count[x] += 1

    dp = [0] * (limit + 1)

    dp[0] = 0
    dp[1] = count[1] * 1

    for i in range(2, limit + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + (count[i] * i))

    return dp[limit]


_ = int(input())
arr = [int(num) for num in input().split()]
print(boredom(arr))
