

def new_years_number(n):
    if n < 2020:
        return "NO"
    ones = n % 2020
    n = n - (ones * 2021)
    if n < 0:
        return "NO"
    return "YES" if n % 2020 == 0 else "NO"


if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(new_years_number(n))