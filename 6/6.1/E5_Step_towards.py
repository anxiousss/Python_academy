from math import cos, sin, dist


def solution(x1, y1, p, q):
    x2 = p * cos(q)
    y2 = p * sin(q)
    print(dist((x1, y1), (x2, y2)))


def main():
    x1, y1 = map(float, input().split())
    p, q = map(float, input().split())
    solution(x1, y1, p, q)


if __name__ == '__main__':
    main()
