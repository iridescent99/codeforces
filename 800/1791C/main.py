
def prepend_and_append(s):
    while len(s) > 1 and s[0] != s[-1]:
        s = s[1:-1]
    return len(s)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(prepend_and_append(s))