import math


def dreamoon_and_wifi(s1, s2):
    n = len(s1)

    desired = [1 if s == "+" else -1 for s in s1]
    desired_outcome = sum(desired)

    undecided = [i for i, s in enumerate(s2) if s == "?"]
    m = len(undecided)

    def move(total, i):
        if i == n:
            if total == desired_outcome:
                return 1
            return 0
        if s2[i] == "+":
            return move(total + 1, i + 1)
        elif s2[i] == "-":
            return move(total - 1, i + 1)
        elif s2[i] == "?":
            return move(total - 1, i + 1) + move(total + 1, i + 1)

    possible_paths = move(0, 0)

    return possible_paths / math.pow(2, m)


s1 = input()
s2 = input()
print(dreamoon_and_wifi(s1, s2))
