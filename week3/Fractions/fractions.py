class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)


    def __repr__(self):
        return self.__str__()

    def num_from_frac(self):
        self.numerator = float(self.numerator)
        return self.numerator / self.denominator

    def __add__(self, other):
        # check for division by zero
        # if self.numerator == 0 or self.denominator == 0 or \
        #     other.numerator == 0 or other.denominator == 0:
        #     return "Uhooo division by 0 here"
        return int(self.num_from_frac() + other.num_from_frac())

    def __sub__(self, other):
        return int(self.num_from_frac() - other.num_from_frac())

    def __mul__(self, other):
        return str("{} / {}".format(self.numerator, other.denominator))

    def __eq__(self, other):
        return True if self.num_from_frac() == other.num_from_frac() else False




# a = Fraction(1, 2)
# b = Fraction(2, 4)
# print(a == b)
# # print(dir(2))
