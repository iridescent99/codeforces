

def pythagorean_triples(n):
    # n**2 = (c-b)(c+b)
    if n % 2 != 0:
        c = (n**2 + 1) // 2
        b = c - 1
    else:
        c = n**2 // 4 + 1
        b = c - 2
    if b == 0 or c == 0:
        return -1,
    return b, c


n = int(input())
print(*pythagorean_triples(n))