from bisect import bisect_right, insort


def can_win_k(a, k):
    ms = sorted(a)

    for t in range(k, 0, -1):
        idx = bisect_right(ms, t) - 1
        if idx < 0:
            return False
        ms.pop(idx)

        if ms:
            x = ms.pop(0) + t
            insort(ms, x)

    return True


def number_game(a):
    n = len(a)
    for k in range(n, -1, -1):
        if can_win_k(a, k):
            return k
    return 0


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().split()))
        print(number_game(a))
