import math

def is_palindrome(s):
    half = math.ceil(len(s) / 2)
    return s[:half] == s[len(s)-half:]

def beautiful_string(s):
    left,right=0,1
    while left < right < len(s):
        if s[left] < s[right] and s[right-1] < s[right]:
            if is_palindrome(s[:left] + s[right:]):
                print(right-left)
                print(s[left:right])
            right += 1
        else:
            left += 1
            right = left + 1

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = [int(n) for n in input()]
        beautiful_string(s)