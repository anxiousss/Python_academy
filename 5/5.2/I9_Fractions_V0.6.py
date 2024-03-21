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
            if isinstance(args[0], str) and '/' in args[0]:
                s = args[0].split('/')
                self.num, self.denom = map(int, s)
            elif isinstance(args[0], str) and '/' not in args[0]:
                s = args[0]
                self.num, self.denom = int(s), 1
            elif isinstance(args[0], int):
                s = args[0]
                self.num, self.denom = s, 1
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

    def reverse(self):
        return Fraction(self.denom, self.num)

    def __str__(self):
        return f'{self.num}/{self.denom}'

    def __repr__(self):
        return f"Fraction('{self.num}/{self.denom}')"

    def __neg__(self):
        return Fraction(-self.num, self.denom)

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_num = other.num * self.denom + self.num * other.denom
            new_denom = other.denom * self.denom
            return Fraction(new_num, new_denom)

        new_num = other * self.denom + self.num
        return Fraction(new_num, self.denom)

    def __iadd__(self, other):
        if isinstance(other, Fraction):
            self.num = other.num * self.denom + self.num * other.denom
            self.denom *= other.denom
            self.__reduction()
            return self

        self.num += other * self.denom
        self.__reduction()
        return self

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.denom - self.denom * other.num
            new_denom = other.denom * self.denom
            return Fraction(new_num, new_denom)

        new_num = self.num - other * self.denom
        return Fraction(new_num, self.denom)

    def __isub__(self, other):
        if isinstance(other, Fraction):
            self.num = self.num * other.denom - self.denom * other.num
            self.denom *= other.denom
            self.__reduction()
            return self

        self.num -= other * self.denom
        self.__reduction()
        return self

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.num
            new_denom = self.denom * other.denom
            return Fraction(new_num, new_denom)

        new_num = self.num * other
        return Fraction(new_num, self.denom)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            new_num = self.num * other.denom
            new_denom = self.denom * other.num
            return Fraction(new_num, new_denom)

        new_denom = self.denom * other
        return Fraction(self.num, new_denom)

    def __imul__(self, other):
        if isinstance(other, Fraction):
            self.num *= other.num
            self.denom *= other.denom
            self.__reduction()
            return self

        self.num *= other
        self.__reduction()
        return self

    def __itruediv__(self, other):
        if isinstance(other, Fraction):
            self.num *= other.denom
            self.denom *= other.num
            self.__reduction()
            return self

        self.denom *= other
        self.__reduction()
        return self

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denom == self.denom * other.num

        return self.num / self.denom == other

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.num * other.denom > self.denom * other.num

        return self.num / self.denom > other

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return not self > other

    def __ne__(self, other):
        return not self == other
