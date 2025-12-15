
def discounts(n, k, prices, discount):
    discount.sort()
    prices.sort()
    bought = len(prices)
    for d in discount:
        free = bought - d
        if 0 <= free:
            prices.pop(free)
            bought -= d
    return sum(prices)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, k = [int(num) for num in input().split()]
        prices = [int(num) for num in input().split()]
        vouchers = [int(num) for num in input().split()]
        print(discounts(n, k, prices, vouchers))