def prefix_min_suffix_max(n, arr):
    result = ""
    prefix_min = [0] * n
    prefix_min[0] = arr[0]
    suffix_max = [0] * n
    suffix_max[-1] = arr[-1]
    for i in range(1, n):
        prefix_min[i] = min(prefix_min[i-1], arr[i])
    for i in range(n-2, -1, -1):
        suffix_max[i] = max(suffix_max[i+1], arr[i])
    for i in range(n):
        exists = "1"
        if not (prefix_min[i] == arr[i] or arr[i] == suffix_max[i]):
            exists = "0"
        result += exists
    return result


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = [int(num) for num in input().split()]
        print(prefix_min_suffix_max(n, arr))