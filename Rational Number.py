class RationalNumbers:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        self.value = self.numerator / self.denominator

    def __repr__(self):
        return f"Fraction {self.numerator}/{self.denominator}"

    def __pos__(self):
        return self

    def __neg__(self):
        self.numerator *= -1
        return self

    def __abs__(self):
        self.numerator = abs(self.numerator)
        self.denominator = abs(self.denominator)
        self.value = abs(self.value)

    def __round__(self, n=None):
        if self.value >= 0:
            if (self.value - int(self.value)) >= 0.5:
                self.value = int(self.value + 1)

            else:
                self.value = int(self.value)

            self.numerator = self.value
            self.denominator = 1

        else:
            if abs(self.value - int(self.value)) >= 0.5:
                self.value = -int(abs(self.value + 1))

            else:
                self.value = int(abs(self.value))

            self.numerator = self.value
            self.denominator = 1

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return self.value

    def __add__(self, other):

        if isinstance(other, RationalNumbers):

            if self.denominator != other.denominator:
                new_fraction = RationalNumbers(self.numerator * other.denominator + other.numerator * self.denominator,
                                               self.denominator * other.denominator)
            else:
                new_fraction = (self.numerator + other.numerator, self.denominator)
            return new_fraction

        elif isinstance(other, (float, int)):
            return other + self.numerator / self.denominator

        else:
            raise ValueError("can`t add")

    def __ge__(self, other):
        if isinstance(other, RationalNumbers):
            return self.value >= other.value
        elif isinstance(other, (float, int)):
            return self.numerator / self.denominator >= other
        else:
            raise ValueError("can`t compare")

    def __eq__(self, other):
        return self.value == other.value

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            new_fraction = RationalNumbers(self.numerator ** power, self.denominator ** power)
        # if isinstance(power, RationalNumbers):
        #     new_fraction = RationalNumbers(self.numerator**power.value, self.denominator**power.value)
        # elif isinstance(power,(int, float)):
        #     new_fraction = (self.numerator**power, self.denominator**power)
        else:
            raise ValueError('can`t raise to that power')
        return new_fraction

    def __mul__(self, other):

        if isinstance(other, RationalNumbers):
            new_fraction = (self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int):
            new_fraction = (self.numerator * other, self.denominator)
        else:
            raise ValueError('can`t multiply')
        return new_fraction

    def __sub__(self, other):
        return self.__add__(-other)

    def __truediv__(self, other):
        if isinstance(other, RationalNumbers):
            inverse_fraction = RationalNumbers(other.denominator, other.numerator)
            return self * inverse_fraction
        elif isinstance(other, int):
            return RationalNumbers(self.numerator, self.denominator * other)
        else:
            raise ValueError('can`t divide')


F1 = RationalNumbers(1, 3)
F2 = RationalNumbers(2, 3)
