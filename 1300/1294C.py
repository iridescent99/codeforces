import math


def product_of_three_numbers(n):
    a = b = c = 0
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            a = i
            n //= a
            break
    if a == 0:
        print("NO")
        return
    for i in range(a + 1, int(math.sqrt(n)) + 1):
        if n % i == 0 and i != a:
            c = n // i
            if c > 1 and c not in [i,a]:
                print("YES")
                print(a, i, c)
                return
    print("NO")


t = int(input())
for _ in range(t):
    n = int(input())
    product_of_three_numbers(n)
