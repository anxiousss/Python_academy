from math import pi, e, log, pow, cos, sin


def f(x):
    first_degree = 3 / 16
    arg = (pi * x) / (2 * e)
    second_degree = cos(arg)
    print(log(pow(x, first_degree), 32) + pow(x, second_degree) - pow(sin(x / pi), 2))


def main():
    x = float(input())
    f(x)


if __name__ == '__main__':
    main()
