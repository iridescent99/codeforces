
def renako_amaori(a, b, n):
    for i in range(n):
        if i % 2 == 0:
            if a[i] < b[i]:
                a[i],b[i] = b[i],a[i]
        else:
            if b[i] < a[i]:
                a[i],b[i] = b[i],a[i]
    sA = (a)
    sB = sum(b)
    return "Ajisai" if sA > sB else "Mai" if sB > sA else "Tie"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        print(renako_amaori(a, b, n))