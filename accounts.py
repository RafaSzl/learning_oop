import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        # w dwoch krokach mam czas lokalny: 1. modul datetime pokazuje date w utc
        # i potem pytz zamienia to w czas lokalny
        #undersore w tej method pokazuje ze to nie jest do uzycia poza klasa
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for" + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            # self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow()), amount))
            # i tutaj zamiast self._current_time() mam Account bo to jest static
            # method i dzieki temu python nie szuka po instancjach i pozniej po klasach tylko od razu po klasach
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Cant withdraw more than you have")
            self.show_balance()
        elif amount < 0:
            print("Cant withdraw values below 0")
            self.show_balance()
        else:
            self.balance -= amount
            # self.show_balance()
            self.transaction_list.append((Account._current_time(), -amount))

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {}".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = Account("Tim", 0)
    tim.show_balance()

    tim.deposit(1000)

    tim.withdraw(900)

    tim.show_transactions()

    steph = Account("Steph", 800)
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
