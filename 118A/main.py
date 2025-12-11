def transform(w):
    vowels = 'aoyeuiAOYEUI'
    word = ""
    for letter in w:
        if letter not in vowels:
            word += "." + letter.lower()
    print(word)


if __name__ == "__main__":
    word = input()
    transform(word)
