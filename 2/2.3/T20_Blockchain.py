def blockchain(N):
    h = 0
    blockchain_right = True
    for i in range(N):

        if i == 0:
            h_1 = 0

        else:
            h_1 = h

        b_n = int(input())
        h = b_n % 256
        b_n //= 256
        r = b_n % 256
        b_n //= 256
        m = b_n

        if ((h != 37 * (m + r + h_1) % 256) or (h >= 100)) and blockchain_right:
            print(i)
            blockchain_right = False

    if blockchain_right:
        print('-1')


def main():
    N = int(input())
    blockchain(N)


if __name__ == '__main__':
    main()
