
def copy(n, arr):
    return len(set(arr))


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(num) for num in input().split()]
    print(copy(n, arr))
