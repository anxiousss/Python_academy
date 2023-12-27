def solution(n_racers):
    racer = 1
    seconds = 3
    for i in range(n_racers):

        for j in range(seconds, 0, - 1):
            print(f"До старта {j} секунд(ы)")

        print(f'Старт {racer}!!!')
        racer += 1
        seconds += 1


def main():
    n_racers = int(input())
    solution(n_racers)


if __name__ == '__main__':
    main()
