

def basketball_exercise(h1, h2, n):
    dp = [[0] * 3 for _ in range(n)]
    # 0 is first row 1 is second row 2 is skip
    dp[0][0] = h1[0]
    dp[0][1] = h2[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1] + h1[i], dp[i-1][2] + h1[i])
        dp[i][1] = max(dp[i-1][0] + h2[i], dp[i-1][2] + h2[i])
        dp[i][2] = max(dp[i-1][2], max(dp[i-1][0], dp[i-1][1]))
    return max(dp[n-1][0], dp[n-1][1])



n = int(input())
h1 = [int(num) for num in input().split()]
h2 = [int(num) for num in input().split()]
print(basketball_exercise(h1, h2, n))