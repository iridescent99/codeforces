
def minimise_sum(n, arr):
    prefMin = [0] * n
    prefMin[0] = arr[0]
    existsSafePrefix = [False] * n
    suffixSum = [0] * (n+1)
    suffixSum[n] = 0
    for i in range(1, n):
        prefMin[i] = min(prefMin[i-1], arr[i])
        existsSafePrefix[i] = existsSafePrefix[i-1] or arr[i] > prefMin[i-1]
    for i in range(n-1, -1, -1):
        suffixSum[i] = prefMin[i] + suffixSum[i+1]
    total = suffixSum[0]
    bestValue = total
    for i in range(1,n):
        if existsSafePrefix[i-1]:
            candidate = total - suffixSum[i]
            if candidate < bestValue:
                bestValue = candidate
    return bestValue


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = [int(num) for num in input().split()]
        print(minimise_sum(n, A))