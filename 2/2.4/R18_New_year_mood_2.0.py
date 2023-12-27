def sol(x):
    row = ''
    ln = [0]
    for j in range(1, (x + 1)):
        row += str(j) + ' '
        if j in (sum(range(i)) for i in range(j + 2)):
            ln.append(len(row) - 1)
            row = ''
    ln.append(len(row) - 1)
    d = 1

    for z in range(1, x + 1):
        if z - 1 in (sum(range(i)) for i in range(z + 2)):
            print(f"{' ' * ((max(ln) - ln[d]) // 2)}{z}", end=' ' if z != 1 else '\n')
            d += 1
        else:
            print(z, end='\n' if z in (sum(range(i)) for i in range(z + 2)) else ' ')


def main():
    x = int(input())
    sol(x)


if __name__ == '__main__':
    main()
