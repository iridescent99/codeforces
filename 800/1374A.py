def required_remainder(x,y,n):
    max_p = (n-y)//x
    for p in range(max_p, -1, -1):
        if p*x+y <= n:
            return p*x+y
    return 0


t = int(input())
for _ in range(t):
    x, y, n = [int(num) for num in input().split()]
    print(required_remainder(x,y,n))