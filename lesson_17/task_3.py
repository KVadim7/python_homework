class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise TypeError("Знаменник не може дорівнювати нулю")
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def simplify(self):
        common_divisor = self.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __add__(self, other):
        common_denominator = self.denominator * other.denominator
        num_1 = self.numerator * other.denominator
        num_2 = other.numerator * self.denominator
        numerator = num_1 + num_2
        result = Fraction(numerator, common_denominator)
        result.simplify()
        return result

    def __sub__(self, other):
        common_denominator = self.denominator * other.denominator
        num_1 = self.numerator * other.denominator
        num_2 = other.numerator * self.denominator
        numerator = num_1 - num_2
        result = Fraction(numerator, common_denominator)
        result.simplify()
        return result

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Не можна ділити на нуль")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        result = Fraction(numerator, denominator)
        result.simplify()
        return result

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        return not self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        num_1 = self.numerator * other.denominator
        num_2 = other.numerator * self.denominator
        return num_1 < num_2

    def __le__(self, other):
        num_1 = self.numerator * other.denominator
        num_2 = other.numerator * self.denominator
        return num_1 <= num_2

    def __gt__(self, other):
        num_1 = self.numerator * other.denominator
        num_2 = other.numerator * self.denominator
        return num_1 > num_2

    def __ge__(self, other):
        num_1 = self.numerator * other.denominator
        num_2 = other.numerator * self.denominator
        return num_1 >= num_2


x = Fraction(3, 5)
y = Fraction(1, 4)
c = x / y
print(c.numerator)
print(c.denominator)

x = Fraction(20, 5)
y = Fraction(20, 1)
print(x < y)

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)
