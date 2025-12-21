def snake_order(n):
    P = []
    for r in range(n):
        if r % 2 == 0:
            for c in range(n):
                P.append((r, c))
        else:
            for c in range(n-1, -1, -1):
                P.append((r, c))
    return P

def arrow(u, v):
    # u, v are adjacent cells (Manhattan distance 1)
    (r1, c1), (r2, c2) = u, v
    if r2 == r1 and c2 == c1 + 1: return 'R'
    if r2 == r1 and c2 == c1 - 1: return 'L'
    if c2 == c1 and r2 == r1 + 1: return 'D'
    if c2 == c1 and r2 == r1 - 1: return 'U'
    raise ValueError("Non-adjacent in snake")

def arrow_out(u, n):
    # choose any direction that leaves the grid in ONE step
    r, c = u
    if r == 0: return 'U'
    if r == n-1: return 'D'
    if c == 0: return 'L'
    if c == n-1: return 'R'
    raise ValueError("Not on boundary")

def construct(n, k):
    N = n*n
    P = snake_order(n)
    grid = [['U'] * n for _ in range(n)]

    # Escape component
    if k > 0:
        E = P[0]
        grid[E[0]][E[1]] = arrow_out(E, n)
        for i in range(1, k):
            u, v = P[i], P[i-1]
            grid[u[0]][u[1]] = arrow(u, v)

    # Sink component
    if N - k >= 2:
        u, v = P[N-2], P[N-1]
        grid[u[0]][u[1]] = arrow(u, v)
        grid[v[0]][v[1]] = arrow(v, u)
        for i in range(k, N-2):
            u, v = P[i], P[i+1]
            grid[u[0]][u[1]] = arrow(u, v)

    
    for row in grid:
        print(*row)


t = int(input())
for _ in range(t):
    n, k = [int(num) for num in input().split()]
    construct(n, k)
