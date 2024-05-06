def decimalTobinary(n):
    assert int(n) == n, "the parameter must be an integer only!"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalTobinary(int(n / 2))


if __name__ == "__main__":
    print(decimalTobinary(10))
