def dragons(s, n, lines):
    lines = sorted(lines,  key=lambda t: t[0])
    i = 0
    defeated = 0
    while i < len(lines):
        x, y = lines[i]
        if s > x:
            s += y
            lines.pop(i)
            i = 0
            defeated += 1
        else:
            i += 1
    return "YES" if defeated == n else "NO"


s, n = [int(num) for num in input().split()]
lines = []
for _ in range(n):
    x, y = input().split()
    lines.append((int(x), int(y)))
print(dragons(s, n, lines))
