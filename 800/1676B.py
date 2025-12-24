


def equal_candies(candies):
    min_box = min(candies)
    candies_eaten = 0
    for box in candies:
        candies_eaten += box - min_box
    return candies_eaten


t = int(input())
for _ in range(t):
    n = int(input())
    candies = [int(num) for num in input().split()]
    print(equal_candies(candies))