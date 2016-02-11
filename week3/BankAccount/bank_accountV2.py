class Bill:
    def __init__(self, amount):
        self.is_amount_negative(amount)
        self.is_wrong_type(amount)
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(int(self.amount))

    def __repr__(self):
        return str(self)

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return False if self.amount != other.amount else True

    def __hash__(self):
        return int(self.amount)

    def total(self):
        return int(self.amount)

    def __len__(self):
        return 1

    def is_amount_negative(self, amount):
        if amount < 0:
            raise ValueError

    def is_wrong_type(self, amount):
        if type(amount) != int:
            raise TypeError


class BatchBill:
    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        result = 0
        for item in self.bills:
            result += int(item)
        return result

    def __getitem__(self, index):
        return self.bills[index]




class CashDesk:
    def __init__(self):
        self.money = 0
        self.set = {}

    def update_cashdesk(self, item):
        for i in item:
            if not i in self.set:
                self.set[i] = 1
            else:
                self.set[i] += 1
  


    def take_money(self, money):
        self.money += money.total()
        if len(money) == 1:
            money = [money]
        self.update_cashdesk(money)



    def total(self):
        return self.money


    def inspect(self):
        return self.printing()

    def printing(self):
        line1 = "We have a total of {}$ in the desk".format(self.total()) 
        line2 = "We have the following count of bills, sorted in ascending order:" 
        line3 = ""
        self.set = sorted(self.set)
        for item in self.set:
            line3 += str(item) + '\n'
        return ("{}\n{}\n{}".format(line1, line2, line3))



values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

# desk.take_money(batch)
desk.take_money(Bill(10))

# print(desk.total()) # 390
print(desk.inspect())
