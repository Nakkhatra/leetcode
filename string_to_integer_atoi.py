def myAtoi(s: str) -> int:
    digCount = 0
    mul = 1
    ans = 0
    symCount = 0
    count = 0

    for char in s:
        if digCount < 1:
            if char == " ":
                if symCount < 1:
                    continue
                else:
                    return 0

            elif char == "+" or char == "-":
                symCount += 1
                if symCount >= 2:
                    break
                if char == "-":
                    mul = -1
                continue

            elif char == ".":
                return 0

            elif ord(char) >= 48 and ord(char) <= 57:
                ans = 10 * ans + int(char)
                digCount += 1

            else:
                break

        else:
            if (
                ord(char) >= 48 and ord(char) <= 57
            ):  # NOTE: ord() provides the unicode number for the character, for "0" it is 48 and for "9" it is 57
                ans = 10 * ans + int(char)

            else:
                break

    ans *= mul

    if ans >= 2 ** 31 - 1:
        return 2 ** 31 - 1

    elif ans <= (-2) ** 31:
        return (-2) ** 31

    else:
        return ans


print(myAtoi("42"))
print(myAtoi("  42"))
print(myAtoi("+42"))
print(myAtoi("-42"))
print(myAtoi("++42"))
print(myAtoi("--42"))
print(myAtoi("+-42"))
print(myAtoi("  .42"))
print(myAtoi("+.42"))
print(myAtoi(" - 42"))
print(myAtoi("999999999999999999999999999999999999999"))
print(myAtoi("hello 54 69"))
print(myAtoi("54 words"))
print(myAtoi("  +b12102370352"))
