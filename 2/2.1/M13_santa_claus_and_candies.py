def solution(n_kids, n_candies):
    candies_to_one_kid = n_candies // n_kids
    left_candies = n_candies - candies_to_one_kid * n_kids
    print(candies_to_one_kid)
    print(left_candies)


def main():
    n_kids = int(input())
    n_candies = int(input())
    solution(n_kids, n_candies)


if __name__ == "__main__":
    main()
