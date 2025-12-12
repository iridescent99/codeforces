

def caps_lock(w):
    if len(w) == 1:
        return w.lower() if w == w.upper() else w.upper()
    if w == w.upper():
        return w.lower()
    if w[0] == w[0].lower() and w[1:] == w[1:].upper():
        return w[0].upper() + w[1:].lower()
    return w


if __name__ == "__main__":
    word = input()
    print(caps_lock(word))