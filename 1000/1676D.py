
def xsum(grid, m, n):
    diagonal_sums_up = [[0 for _ in range(m)] for _ in range(n)]
    diagonal_sums_down = [[0 for _ in range(m)] for _ in range(n)]
    max_x_sum = 0

    for i in range(m):
        c = i
        r = 0
        diag_sum = 0
        while c < m and r < n:
            diag_sum += grid[r][c]
            c += 1
            r += 1
        c -= 1
        r -= 1
        while c >= i and r >= 0:
            diagonal_sums_down[r][c] = diag_sum
            c -= 1
            r -= 1

    for i in range(1, n):
        c = 0
        r = i
        diag_sum = 0
        while c < m and r < n:
            diag_sum += grid[r][c]
            c += 1
            r += 1
        c -= 1
        r -= 1
        while c >= 0 and r >= i:
            diagonal_sums_down[r][c] = diag_sum
            c -= 1
            r -= 1

    for i in range(0, n):
        diag_sum = 0
        c = 0
        r = i
        while r >= 0 and c < m:
            diag_sum += grid[r][c]
            c += 1
            r -= 1
        c -= 1
        r += 1
        while c >= 0 and r <= i:
            diagonal_sums_up[r][c] = diag_sum-grid[r][c]
            c -= 1
            r += 1

    for i in range(1, m):
        c = i
        r = n - 1
        diag_sum = 0
        while r >= 0 and c < m:
            diag_sum += grid[r][c]
            c += 1
            r -= 1
        r += 1
        c -= 1
        while r < n and c >= i:
            diagonal_sums_up[r][c] = diag_sum-grid[r][c]
            c -= 1
            r += 1

    for r in range(n):
        for c in range(m):
            max_x_sum = max(max_x_sum, diagonal_sums_up[r][c] + diagonal_sums_down[r][c])
    return max_x_sum


t = int(input())
for _ in range(t):
    n, m = [int(num) for num in input().split()]
    grid = []
    for _ in range(n):
        grid.append([int(num) for num in input().split()])
    print(xsum(grid, m, n))
