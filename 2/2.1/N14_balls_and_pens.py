def solution(reds, greens, blues):
    all_balls = reds + greens + blues
    print(all_balls - greens + 1)


def main():
    reds = int(input())
    greens = int(input())
    blues = int(input())
    solution(reds, greens, blues)


if __name__ == "__main__":
    main()
