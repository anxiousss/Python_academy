def is_prime(N):
    if N < 2:
        return False

    for i in range(2, int(N**0.5 + 1)):
        if N % i == 0:
            return False
    else:
        return True