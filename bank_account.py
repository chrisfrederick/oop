class BankAccount:

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance > 0):
            self.balance -= amount
        else:
            print("insufficent funds")
        return self

    def display_account_info(self):
        print(f"${self.balance}")

    def yield_interest(self):
            self.balance += (self.balance * self.int_rate)
            return self

ba1 = BankAccount()
ba1.display_account_info()
ba1.deposit(300).deposit(200).deposit(1000).withdraw(100).display_account_info()

ba2 = BankAccount()
ba2.display_account_info()
ba2.deposit(500).deposit(500).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()

