

def candies(n):
    for k in range(2,n):
        if n % (2**k - 1) == 0:
            return n // (2**k - 1)
    return 1


t = int(input())
for _ in range(t):
    n = int(input())
    print(candies(n))