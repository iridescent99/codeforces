def boy_or_girl(username):
    hmap = {}
    for letter in username:
        hmap[letter] = hmap.get(letter, 0) + 1
    if len(hmap) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


if __name__ == "__main__":
    username = input()
    boy_or_girl(username)
