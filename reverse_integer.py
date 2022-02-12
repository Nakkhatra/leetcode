# NOTE: I have tried two different solutions and both work fine. But still I prefer the latter approach.


def reversewithstring(x):
    if x == 0:
        return 0
    s = str(abs(x))
    res = ""

    for i in range(len(s) - 1, -1, -1):
        res += s[i]

    ans = (x // abs(x)) * int(res)

    if ans >= (-2) ** 31 and ans <= 2 ** 31 - 1:
        return ans
    else:
        return 0

    # NOTE: You can do it by using the if else condition in one line like this:
    # return (ans <= 2**31-1) * (ans>= (-2)**31) * ans


def reversewithdigit(x):
    n = abs(x)
    digit = 0
    while True:
        digit = digit * 10 + (n % 10)
        if n % 10 == n:
            break
        n //= 10

    if digit >= (-2) ** 31 and digit <= 2 ** 31 - 1:
        return digit * (-1) * (x < 0) + digit * (x >= 0)
    else:
        return 0

    # NOTE: You can do it by using the if else condition in one line like this:
    # return ((digit <= 2**31-1) * (digit >= (-2)**31)) * (digit * (-1) * (x < 0) + digit * (x >= 0))


print(reversewithdigit(-369))
