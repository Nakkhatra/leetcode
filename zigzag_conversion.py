s = "PAYPALISHIRING"
numRows = 3


def zigzag(s, numRows):
    res = ""
    if numRows == 1 or len(s) <= numRows:
        return s
    if len(s) < (numRows + (numRows - 2)):
        numRows
    rem = len(s) % (numRows + (numRows - 2))
    numCols = (
        ((len(s) // (numRows + (numRows - 2))) * (1 + (numRows - 2)))
        if rem == 0
        else (
            (
                (len(s) // (numRows + (numRows - 2))) * (1 + (numRows - 2))
                + 1
                + (rem % numRows)
            )
            if rem < numRows
            else (len(s) // (numRows + (numRows - 2))) * (1 + (numRows - 2))
            + 1
            + (rem % numRows)
        )
    )
    A = [([0] * numCols) for _ in range(numRows)]
    # print(A)
    col = 0
    count = 0

    while col < numCols:
        rem = col % (numRows - 1)
        for row in range(numRows):
            if rem == 0:
                index = count * (2 * numRows - 2) + row
                if index < len(s):
                    A[row][col] = s[index]

        if rem != 0:
            i = (numRows - 1) + (count * (2 * numRows - 2)) + rem
            if i < len(s):
                A[(numRows - 1) - rem][col] = s[i]

        col += 1
        if col % (numRows - 1) == 0:
            count += 1
    # print(A)

    for row in range(numRows):
        for col in range(numCols):
            if A[row][col] != 0:
                res += A[row][col]
    return res, A


if __name__ == "__main__":
    print(zigzag(s, numRows))
