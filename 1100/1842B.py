
def tenzing_and_books(x,n,  s1, s2, s3):
    if x == 0:
        return "Yes"

    i = j = k = 0

    def check(v):
        return (v & ~x) == 0

    cur = 0
    changed = True
    while changed:
        changed = False

        while i < n and check(s1[i]):
            cur |= s1[i]
            changed = True
            i += 1

        while j < n and check(s2[j]):
            cur |= s2[j]
            changed = True
            j += 1

        while k < n and check(s3[k]):
            cur |= s3[k]
            changed = True
            k += 1
    return "Yes" if cur == x else "No"


t = int(input())
for _ in range(t):
    n, x = [int(num) for num in input().split()]
    s1 = [int(num) for num in input().split()]
    s2 = [int(num) for num in input().split()]
    s3 = [int(num) for num in input().split()]
    print(tenzing_and_books(x, n, s1, s2, s3))
