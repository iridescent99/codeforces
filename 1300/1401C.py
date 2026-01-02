def mere_array(n, arr):
    if n == 1:
        return "YES"
    m = min(arr)
    s_arr = sorted(arr)
    for i in range(n):
        if arr[i] % m != 0 and arr[i] != s_arr[i]:
            return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(num) for num in input().split()]
    print(mere_array(n, arr))