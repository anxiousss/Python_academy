def solution(a, b):
    div = a % b

    while div != 0:
        a = div
        div = b % div
        b = a

    return b


def gcd(*seq):
    if len(seq) == 1:
        return seq[0]

    else:

        first, second = seq[0], seq[1]
        ans = solution(first, second)
        for i in range(2, len(seq)):
            a = seq[i]
            ans = solution(ans, a)

    return ans
