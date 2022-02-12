#NOTE: This is still not solved. Will finish this later.

s = "42"

# NOTE: examples:
# " 0-241" -> 0
# "+-42" -> 0
# "++42" -> 0
# "00092" -> 92
# " 0.42" -> 0
# "   -36 word" -> -36


def myAtoi(s: str) -> int:
    neg = 1
    ans = 0
    count = 0
    c = 0
    for char in s:
        if count > 1:
            break
        if c < 1:
            if char == "+" or char == "-":
                count += 1
            if char == "+" or char == " ":
                if ans == 0:
                    continue
                else:
                    break
            elif char == "-":
                if ans == 0:
                    neg = -1
                else:
                    break

        try:
            ans = ans * 10 + int(char)
            c += 1
        except:
            break
    ans *= neg

    if ans < (-2) ** 31:
        ans = (-2) ** 31
    elif ans > 2 ** 31 - 1:
        ans = 2 ** 31 - 1

    return ans


print(myAtoi(s))


# Testcases:

# "42"
# ".42"
# "  9-21474836948hello0"
# "4 2"
# "4+2"
# "5.2"
# "6++41"
# " ++42"
# "000-92"
