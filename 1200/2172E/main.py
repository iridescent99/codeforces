from itertools import permutations


def calc(n, j, k):
    digits = list(str(n))
    perm = list(permutations(digits))
    perm.sort()
    code1 = "".join(list(perm[j-1]))
    code2 = "".join(list(perm[k-1]))
    A = 0
    for i in range(len(code1)):
        if code1[i] == code2[i]:
            A += 1
            continue
    print(str(A) + "A" + str(len(digits)-A) + "B")


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        n, j, k = [int(num) for num in input().split()]
        calc(n, j, k)
