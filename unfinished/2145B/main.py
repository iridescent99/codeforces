
def gen_str(n, actions):
    start = n * ["+"]
    left, right = 0, n - 1
    unknowns = 0
    for action in actions:
        if action == "1":
            start[right] = "-"
            right -= 1
        elif action == "2":
            if len(start) == 1:
                start[left] = "-"
                break
            unknowns += 1
        else:
            start[left] = "-"
            left += 1
    while unknowns > 0 and len(start) > 2:
        start[left] = "?"
        start[right] = "?"
        left += 1
        right -= 1
        unknowns -= 1
    print("".join(start))


if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        n, _ = [int(num) for num in input().split()]
        actions = input()
        gen_str(n, actions)
