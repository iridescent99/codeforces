import sys
sys.setrecursionlimit(300000)

n, m = [int(num) for num in sys.stdin.readline().split()]
tree = [int(v) for v in sys.stdin.readline().split()]
edges = {}
for _ in range(n - 1):
    x, y = [int(e) for e in sys.stdin.readline().split()]
    xedge = edges.get(x, [])
    yedge = edges.get(y, [])
    xedge.append(y)
    yedge.append(x)
    edges[x] = xedge
    edges[y] = yedge


def traverse(tree, edges, prev, i, cats):
    if cats + tree[i] > m:
        return 0
    paths = 0
    has_children = False
    for child in edges[i + 1]:
        if child - 1 != prev and child != i + 1:
            has_children = True
            paths += traverse(tree, edges, i, child - 1, cats + tree[i] if tree[i] else 0)
    if not has_children and i != 0:
        return 1
    return paths


print(traverse(tree, edges, 0, 0, 0))
