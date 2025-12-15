
def move_to_end(n, arr):
    prefix_max = arr[:]
    ans = [0 for i in range(n)]
    for i in range(1, n):
        prefix_max[i] = max(prefix_max[i-1], prefix_max[i])
    suffix_sum = [0 for i in range(n+1)]
    suffix_sum[-1] = 0
    for i in range(n-1, -1, -1):
        suffix_sum[i] = suffix_sum[i+1] + arr[i]
    for k in range(1, n+1):
        ans[k-1] = suffix_sum[n-k+1] + prefix_max[n-k]
    print(*ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = [int(num) for num in input().split()]
        move_to_end(n, A)