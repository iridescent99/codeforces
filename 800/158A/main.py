def calc(arr, kth):
    print(sum([1 if i >= kth and i > 0 else 0 for i in arr]))


if __name__ == "__main__":
    k = int(input().split()[1])
    A = [int(n) for n in input().split()]
    calc(A, A[k-1])
