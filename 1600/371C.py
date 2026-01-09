import sys
import math

hamburger = sys.stdin.readline().strip()
kitchen = [int(i) for i in sys.stdin.readline().split()]
prices = [int(p) for p in sys.stdin.readline().split()]
r = int(sys.stdin.readline())

count = {"B": 0, "S": 0, "C": 0}
for item in hamburger:
    count[item] += 1

make = {"B": kitchen[0], "S": kitchen[1], "C": kitchen[2]}
prices = {"B": prices[0], "S": prices[1], "C": prices[2]}
price = sum([p * i for p, i in zip(prices.values(), count.values())])


def can_make(x, r):
    for i in ["B", "S", "C"]:
        needed = x * count[i]
        if needed <= make[i]:
            needed = 0
        else:
            needed -= make[i]
        r -= (needed * prices[i])
    return r >= 0


left = 0
right = 10 ** 13
while left < right:
    mid = (math.ceil((right - left) / 2)) + left
    if can_make(mid, r):
        left = mid
    else:
        right = mid - 1

print(left)
