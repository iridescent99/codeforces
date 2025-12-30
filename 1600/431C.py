
def ktree(n, k, d):
    MOD = 10**9 + 7
    dp = [[0] * 2 for _ in range(0, n+2)]
    dp[0][0] = 1
    # 0 invalid 1 valid
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i - j < 0:
                break
            prev_weight = i - j
            if j < d:
                dp[i][0] = (dp[prev_weight][0] + dp[i][0]) % MOD
                dp[i][1] = (dp[prev_weight][1] + dp[i][1]) % MOD
            else:
                dp[i][1] = (dp[i][1] + dp[prev_weight][0]) % MOD
                dp[i][1] = (dp[i][1] + dp[prev_weight][1]) % MOD
    return dp[n][1]


n, k, d = [int(num) for num in input().split()]
print(ktree(n, k, d))