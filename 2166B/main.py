def count_moves(a, b, n):
    if n * b <= a or b == a:
        print("1")
        return
    print("2")
    return


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, b, n = [int(l) for l in input().split()]
        (count_moves(a, b, n))
