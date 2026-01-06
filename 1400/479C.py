import sys

iterator = iter(sys.stdin.read().split())
n = int(next(iterator))
exams = []
for _ in range(n):
    a = int(next(iterator))
    b = int(next(iterator))
    exams.append((a, b))

exams.sort()
current_day = -1
for scheduled, early in exams:
    if early >= current_day:
        current_day = early
    else:
        current_day = scheduled

print(current_day)