import sys

n = int(sys.stdin.readline())

topics_teacher = [int(i) for i in sys.stdin.readline().split()]
topics_student = [int(i) for i in sys.stdin.readline().split()]

D = [a - b for a, b in zip(topics_teacher, topics_student)]

pairs = 0
D.sort()

l = 0
r = n-1
while l < r:
    if D[l] + D[r] > 0:
        pairs += (r-l)
        r -= 1
    else:
        l += 1


print(pairs)

