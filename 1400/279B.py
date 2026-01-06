import sys

input = iter(sys.stdin.readline().split())

n = int(next(input))
t = int(next(input))

reading_time = [int(n) for n in sys.stdin.readline().split()]
r = 0
max_num_books = 0
curr_reading_total = 0
for l in range(n):

    while r < n and curr_reading_total + reading_time[r] <= t:
        curr_reading_total += reading_time[r]
        r += 1

    if r - l > max_num_books:
        max_num_books = r - l

    curr_reading_total -= reading_time[l]

print(max_num_books)
