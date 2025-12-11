def codeword():
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        print(word[0] + str(len(word) - 2) + word[-1])


if __name__ == "__main__":
    n = int(input())
    print(n)
    for _ in range(n):
        codeword()
