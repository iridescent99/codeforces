

def two_buttons(n, m):

    moves = 0
    while m > n:
        if m % 2 == 0:
            m //= 2
        else:
            m += 1
        moves += 1
    moves += (n-m)
    return moves


n, m = [int(num) for num in input().split()]
print(two_buttons(n, m))