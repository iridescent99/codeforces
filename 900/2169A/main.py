import math


def alice_and_bob(n, a, bag):
    bag.sort()
    b_left_max = 0
    b_right_max = 0
    b_left = a-1
    b_right = a+1
    for i in range(n):
        if abs(bag[i] - a) > abs(bag[i] - b_left):
            b_left_max += 1
        if abs(bag[i] - a) > abs(bag[i] - b_right):
            b_right_max += 1
    return b_left if b_left_max > b_right_max else b_right


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, a = [int(num) for num in input().split()]
        bag = [int(num) for num in input().split()]
        print(alice_and_bob(n, a, bag))
