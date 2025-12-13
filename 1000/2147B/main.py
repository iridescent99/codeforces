def multiple_construction(n):
    arr = [-1 for _ in range(n)] * 2
    ind = 0
    for num in range(n, 0, -1):
        while ind < len(arr) and arr[ind] != -1:
            ind += 1
        if ind < len(arr):
            multiple = ind + num
            while multiple <= n and arr[multiple] != -1:
                multiple += num
            arr[ind] = num
            arr[multiple] = num
            ind += 1
    for num in arr:
        print(str(num), end=" ")
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        multiple_construction(n)
