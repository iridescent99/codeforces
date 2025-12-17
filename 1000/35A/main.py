import sys

def shell_game(index, swaps):
    for a, b in swaps:
        if index == a:
            index = b
        elif index == b:
            index = a
    return index


if __name__ == "__main__":
    # Redirecting stdin and stdout to the required files
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    try:
        line1 = sys.stdin.readline()
        if not line1:
            exit()

        index = int(line1.strip())
        swaps = []
        for _ in range(3):
            line = sys.stdin.readline()
            if line:
                a, b = map(int, line.split())
                swaps.append((a, b))

        print(shell_game(index, swaps))
    finally:
        sys.stdin.close()
        sys.stdout.close()
