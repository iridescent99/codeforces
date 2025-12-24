

def cypher(n, arr, moves):
    for i in range(n):
        s = sum(moves[i])
        arr[i] += s
        arr[i] %= 10
    return arr


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(num) for num in input().split()]
    moves = []
    for _ in range(n):
        _, mvs = input().split()
        mvs = [-1 if move == "U" else 1 for move in mvs]
        moves.append(mvs)
    print(*cypher(n, arr, moves))