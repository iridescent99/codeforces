


def helpful_maths(s):
    if len(s) == 1:
        return s
    numbers = []
    for i in range(0, len(s), 2):
        numbers.append(int(s[i]))
    numbers.sort()
    return "+".join([str(num) for num in numbers])

s = input()
print(helpful_maths(s))