


def even_modulo_pair(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[j] % arr[i]) % 2 == 0:
                return str(arr[i]) + " " + str(arr[j])
    return -1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = [int(n) for n in input().split()]
        print(even_modulo_pair(l))