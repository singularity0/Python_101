class BankAccount:
    def __init__(self, name, bal, currency):
        self._balance = bal
        self.name = name
        self.currency = currency
        self._history = ["Account was created"]
        self.check_if_Negative(self._balance)

    def check_if_Negative(self, value):
        if value < 0:
            raise ValueError("The value is negative. Action not allowed")

    def deposit(self, amount):
        self.check_if_Negative(amount)
        self._balance += amount
        self._history.append("Deposited {}$".format(amount))
        return self._balance

    def balance(self):
        self._history.append("Balance check -> {}$".format(self._balance))
        return self._balance

    def withdraw(self, amount):
        self._history.append("{}$ was withdrawed".format(amount))
        amount = amount
        if self._balance >= amount:
            self._balance -= amount
            return True
        else:
            return False

    def __str__(self):
        message = "Bank account for {} with balance of {}{}" \
            .format(self.name, self._balance, self.currency)
        return message

    def __int__(self):
        self._history.append("__int__ check -> {}$".format(self._balance))
        return self._balance

    def transfer_to(self, account, amount):
        if self._balance >= amount:
            if self.currency == account.currency:
                self._balance -= amount
                self._history.append(
                    "The amount of {} transferred to the {} account".format(amount, account.name))
                account._history.append(
                    "Recevied {} from source {}".format(amount, self.name))
                account._balance += amount
                return True
            else:
                return False
        return False

    def __repr__(self):
        return 1000

    def history(self):
        # self._history.append("History of {} account called".format(self.name))
        return self._history
