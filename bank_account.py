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



class User:
    bank_name = "Chris' Bank of Eternal Debt"

    def __init__(self, name, email):
        self.name =name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def deposit(self, amount):
        self.account.deposit(amount)
        return self

    def withdrawl(self, amount):
        self.account.withdraw(amount)
        return self

    def display_balance(self):
        print(self.account.display_account_info())
        return self


chris = User("Christopher Frederick", "chris@email.com")
nysha = User("Nysha Sims", "nysha@wmail.com")

chris.deposit(600).deposit(18000).display_balance()
nysha.deposit(700).withdrawl(100).deposit(700).display_balance()