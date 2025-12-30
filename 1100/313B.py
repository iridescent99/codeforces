

def ilya_and_queries(s, queries):
    n = len(s)
    prefix_tracker = [0] * n
    for i in range(n-1):
        if s[i] == s[i + 1]:
            prefix_tracker[i] = 1
    prefix_sum = [0] * (n+1)
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + prefix_tracker[i]
    for l, r in queries:
        if l < 1:
            print(prefix_sum[r])
        else:
            print(prefix_sum[r] - prefix_sum[l])


s = input()
m = int(input())
queries = []
for _ in range(m):
    l, r = [int(num) for num in input().split()]
    queries.append((l-1, r-1))
ilya_and_queries(s, queries)