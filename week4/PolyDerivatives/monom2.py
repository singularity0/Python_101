import sys

class Monom:
    def __init__(self, coef=None, var=None, deg=None):
        self.coef = coef
        self.var = var
        self.deg = deg

    # def __str__(self):
    #     return str(self.create_monom())

    # def create_monom(self):
    #     if ((self.coef is None) and (self.var is None) and (self.deg is None)):
    #         print("monom invalids")
    #         monom = None
    #         return monom
    #     if self.coef == 0:
    #         monom = None
    #         return monom
    #     if self.coef:
    #         if self.deg:
    #             monom = str(self.coef) + self.var+ str(self.deg)
    #         else:
    #             if not self.var:
    #                 monom = str(self.coef)
    #             else:
    #                 monom = str(self.coef) + str(self.var)
    #     else:
    #         if self.deg:
    #             monom = self.var + str(self.deg)
    #         else:
    #             monom = self.var
    #     # return monom

class Parsing:

    @staticmethod
    def parsing(monom):

        if 'x' in monom:
            monom_split = monom.split('x')
            monom = Monom(monom_split[0], 'x', monom_split[1][1:])
        else:
            monom = Monom(monom)
        return monom

class Derivative:

    @staticmethod
    def deriving(monom):
        if monom.var is None and monom.deg is None:
            return 0
        if monom.deg is "":
            if monom.coef:
                return monom.coef
            else:
                return 1
        if monom.coef == "":
            monom.coef = 1
        if monom.deg == str(2):
            return str(int(monom.deg)*int(monom.coef)) + monom.var
        return str(int(monom.deg)*int(monom.coef)) + monom.var + "^" + str(int(monom.deg)-1)



class main():


    polynom = sys.argv[1:]

    result = ''

    for monom in polynom:
        if monom != '+':
            parsed_mon = Parsing.parsing(monom)
            derived_mon = Derivative.deriving(parsed_mon)
            result += str(derived_mon)
        else:
            result += monom
    print(result)

if __name__ == '__main__':
    main()
