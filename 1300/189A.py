import itertools


def cut_ribbon(n, a, b, c):
    global_max = 0
    lengths = sorted([a, b, c], reverse=True)
    a, b, c = lengths[0], lengths[1], lengths[2]
    for i in range(n//a+1):
        if a != b:
            for j in range((n-a*i)//b+1):
                rem = n - (a*i + b*j)
                if rem % c == 0:
                    k = rem // c
                    global_max = max(global_max, i+j+k)
        else:
            rem = n - (a * i)
            if rem % c == 0:
                k = rem // c
                global_max = max(global_max, i + k)
    return global_max

n, a, b, c = [int(num) for num in input().split()]
print(cut_ribbon(n, a, b, c))
