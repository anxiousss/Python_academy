def solution(N):
    st = set()

    for i in range(N):
        another_s = input().split()
        for s in another_s:
            st.add(s)

    for word in st:
        print(word)


def main():
    N = int(input())
    solution(N)


if __name__ == '__main__':
    main()
