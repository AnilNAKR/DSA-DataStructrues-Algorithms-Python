def sumofDigits(n):
    assert n >= 0 and int(n) == n, "The digit has to be a positive integer only!"
    if n == 0:
        return n
    else:
        return int(n % 10) + sumofDigits(int(n / 10))


if __name__ == "__main__":
    print(sumofDigits(1234))
