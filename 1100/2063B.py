def best_with_side(seg, outside):
    seg_sorted = sorted(seg, reverse=True)
    out_sorted = sorted(outside)

    base = sum(seg_sorted)
    best = base

    kmax = min(len(seg_sorted), len(out_sorted))
    cur = base
    for k in range(kmax):
        cur = cur - seg_sorted[k] + out_sorted[k]
        if cur < best:
            best = cur
    return best


def subsequence_update(n, l, r, arr):
    l -= 1
    r -= 1
    seg = arr[l:r + 1]

    left_out = arr[:l]
    right_out = arr[r + 1:]

    ans = sum(seg)
    if left_out:
        ans = min(ans, best_with_side(seg, left_out))
    if right_out:
        ans = min(ans, best_with_side(seg, right_out))
    return ans


t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    print(subsequence_update(n, l, r, arr))
