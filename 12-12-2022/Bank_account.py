import datetime


class BankAccount:
    def __init__(self, name: str, branch: str, account_number: int, account_holders: dict,
                 allowed_usd: bool, shekel_balance: float, usd_balance: float, max_credit: int):
        self.name = name
        self.branch = branch
        self.account_number = account_number
        self.account_holders = account_holders
        self.allowed_usd = allowed_usd
        self.shekel_balance = shekel_balance
        self.usd_balance = usd_balance
        self.max_credit = max_credit
        self.transactions = {}
        self.transactions[datetime.datetime.now()] = []

        self.total_income = 0
        self.total_outcome = 0

    def deposit(self, cash):
        self.transactions[datetime.datetime.now()].append('deposit')
        if self.allowed_usd:
            currency = input("USD or Shekels?")
            if currency == 'USD':
                self.usd_balance += cash
                self.total_income += cash * 3.73
            else:
                self.shekel_balance += cash
                self.total_income += cash
        else:
          self.shekel_balance += cash
          self.total_income += cash

    def withdraw(self, amount):
        self.transactions[datetime.datetime.now()].append('withdraw')
        if self.shekel_balance + self.max_credit >= amount:
            self.shekel_balance -= amount
            self.total_outcome += amount
            return True
        return False

    def convert(self, cash):
        self.transactions[datetime.datetime.now()].append('convert')
        if self.allowed_usd:
            currency = input("Do you want to convert shekels or usd dollars?")
            if currency == "shekels":
                self.usd_balance += cash * 0.27
                self.shekel_balance -= cash
                return True
            else:
                self.shekel_balance += cash * 3.73
                self.usd_balance -= cash
                return True
        else:
            print("You don't have premission to convert to usd $!")
            return False

    def balance(self):
        self.transactions[datetime.datetime.now()].append('balance')
        if self.allowed_usd:
            return [self.usd_balance, self.shekel_balance]
        else:
            return self.shekel_balance

    def transactions(self, date):
        return self.transactions[date]