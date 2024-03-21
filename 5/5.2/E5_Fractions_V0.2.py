from math import gcd


class Fraction:

    def __reduction(self):
        if self.denom < 0:
            self.num *= -1
            self.denom *= -1

        x = gcd(self.num, self.denom)
        self.num = self.num // x
        self.denom = self.denom // x

    def __init__(self, *args):
        if len(args) == 1:
            s = args[0]
            self.num, self.denom = map(int, s.split('/'))
        else:
            self.num, self.denom = map(int, args)

        self.__reduction()

    def numerator(self, n=None):
        if n is None:
            return abs(self.num)

        self.num = (self.num * n) // (abs(self.num))
        self.__reduction()

    def denominator(self, d=None):
        if d is None:
            return self.denom

        self.denom = d
        self.__reduction()

    def __str__(self):
        return f'{self.num}/{self.denom}'

    def __repr__(self):
        return f"Fraction('{self.num}/{self.denom}')"

    def __neg__(self):
        return Fraction(-self.num, self.denom)
