def iterative_update(tree, p, b, n):
    idx = (1 << n) + p - 1
    tree[idx] = b
    is_or = True
    while idx > 1:
        idx //= 2 # Move to parent
        if is_or:
            tree[idx] = tree[2*idx] | tree[2*idx+1]
        else:
            tree[idx] = tree[2*idx] ^ tree[2*idx+1]
        is_or = not is_or
    print(tree[1])


def xenia_and_bit_operations(n, arr, queries):
    size = 1 << n  # 2**n
    tree = [0] * size + arr
    is_or = False
    for i in range(size - 1, 0, -1):
        if (i + 1).bit_count() == 1:
            is_or = not is_or

        if is_or:
            tree[i] = tree[2 * i] | tree[2 * i + 1]
        else:
            tree[i] = tree[2 * i] ^ tree[2 * i + 1]

    for p, b in queries:
        iterative_update(tree, p, b, n)


n, m = [int(num) for num in input().split()]
arr = [int(num) for num in input().split()]
queries = []
for _ in range(m):
    p, b = [int(num) for num in input().split()]
    queries.append((p, b))

xenia_and_bit_operations(n, arr, queries)
