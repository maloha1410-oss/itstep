class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def show_balance(self):
        print(f"Баланс рахунку: {self.balance:.2f} грн")

    def add_money(self, amount):
        if amount <= 0:
            print("Помилка! Сума поповнення повинна бути більшою за 0.")
            return

        self.balance += amount
        print(f"Рахунок поповнено на {amount:.2f} грн.")
        self.show_balance()

    def withdraw(self, amount):
        if amount == 0:
            print("Помилка! Неможливо зняти 0 грн.")
            return

        if amount < 0:
            print("Помилка! Сума зняття не може бути від'ємною.")
            return

        if amount <= self.balance:
            self.balance -= amount
            print(f"Знято {amount:.2f} грн.")
            self.show_balance()
        else:
            shortage = amount - self.balance
            print(f"На рахунку недостатньо коштів.")
            print(f"Не вистачає: {shortage:.2f} грн.")

            answer = input("Бажаєте оформити кредит? (y/n): ").lower()

            if answer == "y":
                days = int(input("На скільки днів потрібен кредит? "))

                if days <= 30:
                    percent = 0.03
                else:
                    percent = 0.04

                repayment = shortage * (1 + percent)

                self.balance = 0

                print(f"Кредит видано на суму {shortage:.2f} грн.")
                print(f"Відсоткова ставка: {percent * 100:.0f}%")
                print(f"До повернення: {repayment:.2f} грн.")
            else:
                print("Операцію скасовано.")


account = BankAccount(1000)

account.show_balance()

account.add_money(500)

account.withdraw(0)

account.withdraw(2000)