

def zero_array(n, arr):
    s = sum(arr)
    m = max(arr)
    if s % 2 == 0 and 2*m <= s:
        return "YES"
    return "NO"


n = int(input())
arr = [int(num) for num in input().split()]
print(zero_array(n, arr))