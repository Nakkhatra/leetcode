import math


def isPalindrome(x: int) -> bool:
    if x == 0:
        return True
    elif x < 0:
        return False
    length = math.floor(math.log10(x)) + 1
    mid = length // 2

    dig = []

    power = length - 1

    for i in range(length):
        dig.append(x // 10 ** power)
        x %= 10 ** power
        power -= 1

    c = 0

    if length % 2 != 0:
        c = 1

    while mid + c < length:
        if dig[mid + c - 1 * (length % 2 == 0)] == dig[mid - c]:
            c += 1
            continue

        else:
            return False

    return True


def isPalindromeWithString(x: int) -> bool:
    s = str(x)

    # revS = ""
    # for i in range(len(s) - 1, -1, -1):
    #     revS += s[i]

    revS = s[
        ::-1
    ]  # NOTE: s[::-1] slicing with -1 step is a much faster method to reverse a list/ string

    if s == revS:
        return True

    else:
        return False


print(isPalindrome(2112))
print(isPalindrome(32123))
print(isPalindromeWithString(2112))
print(isPalindromeWithString(321123))
print(isPalindrome(1))
print(isPalindromeWithString(1))
print(isPalindrome(-1))
print(isPalindromeWithString(-1))
print(isPalindrome(33))
print(isPalindromeWithString(33))
print(isPalindrome(34))
print(isPalindromeWithString(34))
