

def greg_and_graph(n, graph):
    pass


n = int(input())
graph = []
for _ in range(n):
    row = [int(num) for num in input().split()]
    graph.append(row)
deletes = [int(num) for num in input().split()]
print(greg_and_graph(n, graph))