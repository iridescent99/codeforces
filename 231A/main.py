
def validate():
    num = input().split()
    print(num)
    if sum([int(n) for n in num]) >= 2:
        return 1
    return 0


if __name__ == "__main__":
    n = int(input())
    count = 0
    for _ in range(n):
        count += validate()
    print(count)