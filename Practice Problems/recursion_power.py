def power(base, exp):
    assert exp >= 0 and int(exp) == exp, "The exponent must be positive integer only!"
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)


if __name__ == "__main__":
    print(power(-2.5, 7))
