


def kuriyama_mirais_stones(cost, m, qs):
    cost_ordered = sorted(cost)
    n = len(cost)
    prefix_sum_cost = [0] * n
    prefix_sum_cost[0] = cost[0]
    prefix_sum_cost_ordered = [0] * n
    prefix_sum_cost_ordered[0] = cost_ordered[0]
    for i in range(1, n):
        prefix_sum_cost[i] = prefix_sum_cost[i-1] + cost[i]
        prefix_sum_cost_ordered[i] = prefix_sum_cost_ordered[i-1] + cost_ordered[i]
    for i in range(m):
        tp, l, r = qs[i]
        arr = prefix_sum_cost if tp == 1 else prefix_sum_cost_ordered
        if l == 1:
            print(str(arr[r-1]))
        else:
            print(str(arr[r-1] - arr[l-2]))


n = int(input())
cost = [int(num) for num in input().split()]
m = int(input())
questions = []
for _ in range(m):
    tp, l, r = input().split()
    questions.append((int(tp), int(l), int(r)))
kuriyama_mirais_stones(cost, m, questions)