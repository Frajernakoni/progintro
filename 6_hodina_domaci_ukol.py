class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("částka vkladu musí být kladná.")
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

        else:
            print("nedostatek prostředků") 
    def describe(self):
        return f"{self.owner}: {self.balance:.2f} Kč"

acc = BankAccount("Jana")
acc.deposit(1000)
acc.withdraw(300)
acc.withdraw(5000)       # Nedostatek prostředků
print(acc.describe())    # Jana: 700.00 Kč                           