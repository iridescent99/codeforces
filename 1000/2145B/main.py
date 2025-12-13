
def deck_of_cards(n, k, actions):
    if k == n:
        return "-" * n
    deck = n * ["+"]
    min_L = sum(1 for a in actions if a == "0")
    max_L = sum(1 for a in actions if a == "0" or a == "2")
    min_R = sum(1 for a in actions if a == "1")
    max_R = sum(1 for a in actions if a == "1" or a == "2")
    l = len(deck)
    for i in range(l):
        if i < min_L or i >= l-min_R:
            deck[i] = "-"
        elif max_L <= i < l - max_R:
            continue
        else:
            deck[i] = "?"
    return "".join(deck)


if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        n, k = [int(num) for num in input().split()]
        actions = input()
        print(deck_of_cards(n, k, actions))
