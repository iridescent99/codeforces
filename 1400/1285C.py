import sys
import math


X = int(sys.stdin.readline().strip())
min_int = math.inf
a = b = -1
for i in range(int(math.sqrt(X)), 0, -1):
    j = X//i
    if X % i == 0 and math.gcd(i, j) == 1:
        max_num = max(i,j)
        if max_num < min_int:
            min_int = max_num
            a = i
            b = j
print(a,b)
