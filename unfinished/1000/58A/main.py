
def chat_room(s):
    ref = ['h','e','l','l','o']
    result = ""
    ind = 0
    while ind+1 < len(s):
        count = 0
        while s[ind+1] == s[ind]:
            count += 1
        result += s[ind] + str(count)
        

    print("YES")


if __name__ == "__main__":
    s = input()
    chat_room(s)


