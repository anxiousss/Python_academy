def gcd(a, b):
    div = a % b

    while div != 0:
        a = div
        div = b % div
        b = a

    return b